from aiogram import Router, types, F
from bot.database.models import save_alerts
import httpx
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from bot.keyboards.menu import main_menu
from bot.services.crypto_api import get_current_price
from bot.keyboards.alerts import direction_buttons

set_router = Router()

class SetAlertStates(StatesGroup):
    waiting_for_coin = State()
    waiting_for_price = State()

coin_aliases = {
    "btc": "bitcoin",
    "eth": "ethereum",
    "usdt": "tether",
    "bnb": "binancecoin",
    "xrp": "ripple",
    "sol": "solana",
    "ada": "cardano",
    "doge": "dogecoin",
    "usdc": "usd-coin",
    "trx": "tron",
    "steth": "lido-staked-ether",
    "matic": "matic-network",
    "dot": "polkadot",
    "avalanche": "avalanche-2",
    "avax": "avalanche-2",
    "link": "chainlink",
    "shib": "shiba-inu",
    "lunc": "terra-luna",
    "busd": "binance-usd",
    "ltc": "litecoin"
}

@set_router.message(F.text == '➕ Set Alert')
async def start_set_alert(message: types.Message, state: FSMContext):
    await message.answer("🪙 Enter the coin (e.g. BTC, ETH):")
    await state.set_state(SetAlertStates.waiting_for_coin)

@set_router.message(SetAlertStates.waiting_for_coin)
async def coin_input_handler(message: types.Message, state: FSMContext):
    coin_input = message.text.strip().lower()
    coin_id = coin_aliases.get(coin_input, coin_input)

    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()

    if not data or coin_id not in data:
        await message.answer("⚠️ Oops, couldn't find that coin.\nPlease double-check the name and try again.")
        return

    await state.update_data(coin_id=coin_id)
    await message.answer("💰 Now enter the target price (e.g. 30000):")
    await state.set_state(SetAlertStates.waiting_for_price)

@set_router.message(SetAlertStates.waiting_for_price)
async def price_input_handler(message: types.Message, state: FSMContext):
    try:
        price = float(message.text.strip())
    except ValueError:
        await message.answer("❗ Invalid price. Enter a number like 25000:")
        return
    data = await state.get_data()
    coin_id = data["coin_id"]
    current = await get_current_price(coin_id)
    if current >= price:
        await message.answer("📈 Whoa! That price is already in the past! The market’s moving fast — try setting a new, higher target. 😉", reply_markup=main_menu)
        await state.clear()
        return

    await save_alerts(message.from_user.id, coin_id, price)
    await message.answer(f"✅ Alert set for {coin_id.upper()} at ${price}", reply_markup=main_menu)
    await state.clear()

