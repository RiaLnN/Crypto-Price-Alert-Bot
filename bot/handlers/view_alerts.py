from aiogram import Router, types, F
from bot.database.queries import get_all_alerts, remove_alert, update_alert_price_in_db
from bot.keyboards.alerts import alert_buttons
from bot.services.crypto_api import get_current_price
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery
from bot.keyboards.menu import main_menu

view_router = Router()
coin_stickers = {
    "bitcoin": "🟠",
    "ethereum": "🔷",
    "litecoin": "💎",
    "dogecoin": "🐶",
    "binancecoin": "🟡",
    "xrp": "💧",
    "cardano": "🌌",
    "solana": "🌈",
    "tron": "🔺",
}
class AlertStates(StatesGroup):
    waiting_new_price = State()

@view_router.message(F.text == '👁 View Alerts')
async def cmd_view(message: types.Message):
    alerts = await get_all_alerts()

    if not alerts:
        await message.answer("📭 You don’t have any alerts set yet.")
        return

    for alert_id, coin_name, price in alerts:
        print(alert_id)
        sticker = coin_stickers.get(coin_name.lower(), "💰")
        await message.answer(
            f"{sticker} <b>{coin_name.upper()}</b>\n\n📈 Target price:  <code>${price}</code>",
            parse_mode="HTML",
            reply_markup=alert_buttons(coin_name, price)
        )

@view_router.callback_query(F.data.startswith("update_"))
async def update_alert_price(callback: CallbackQuery, state: FSMContext):
    alert_id = callback.data.split("_")[1]
    await state.update_data(alert_id=alert_id, user_id=callback.from_user.id)
    await callback.answer("")
    await callback.message.answer("✏️ Enter new price for this alert:")
    await state.set_state(AlertStates.waiting_new_price)

@view_router.message(AlertStates.waiting_new_price)
async def process_new_price(message: Message, state: FSMContext):

    data = await state.get_data()
    coin_name = data["alert_id"]

    try:
        new_price = float(message.text)
        await update_alert_price_in_db(message.from_user.id, new_price, coin_name)
        await message.answer(f"✅ Alert updated for {coin_name.upper()} to ${new_price}", reply_markup=main_menu)
    except ValueError:
        await message.answer("❌ Please enter a valid number.")
        return

    await state.clear()

@view_router.callback_query(F.data.startswith("delete_"))
async def delete_alert(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    coin_name = callback.data.split("_")[1]
    price = float(callback.data.split("_")[2])
    await remove_alert(user_id, coin_name, price)
    await callback.answer("✅ Alert deleted")
    await callback.message.edit_text("🗑️ Alert deleted.")

@view_router.callback_query(F.data.startswith("view_"))
async def view_current_price(callback: types.CallbackQuery):
    coin = callback.data.split("_")[1]
    current = await get_current_price(coin)
    await callback.answer("")
    await callback.message.answer(f"📊 Current price of <b>{coin.upper()}</b>: <code>${current}</code>", parse_mode="HTML")
