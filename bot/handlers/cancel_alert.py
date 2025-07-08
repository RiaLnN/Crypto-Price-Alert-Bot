from aiogram import Router, types, F
from bot.database.queries import remove_all
from bot.keyboards.alerts import delete_buttons
from bot.database.queries import get_all_alerts
clear_router = Router()

@clear_router.message(F.text == '❌ Cancel All')
async def cmd_clear(message: types.Message):
    alerts = await get_all_alerts()

    if not alerts:
        await message.answer("📭 You don’t have any alerts to cancel.")
        return
    await message.answer("Are you sure you want to remove all alerts?:", reply_markup=delete_buttons())


@clear_router.callback_query(F.data == "warning")
async def delete_all(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    await remove_all(user_id)
    await callback.answer("✅ canceled")
    await callback.message.answer("✅ All alerts was successfully canceled")

