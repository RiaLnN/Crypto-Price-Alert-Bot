from aiogram import Router, types, F


help_router = Router()

@help_router.message(F.text == 'ℹ️ Help')
async def help_command(message: types.Message):
    await message.answer(
        "🧠 <b>Crypto Alert Bot – Help Menu</b>\n\n"
        "Here's what I can do for you:\n\n"
        "<b>➕ Set Alert</b>\n"
        "Start tracking a cryptocurrency. I’ll notify you when the price hits your target.\n"
        "• Example: Press '➕ Set Alert' and follow the steps.\n\n"
        "<b>📊 View Alerts</b>\n"
        "See all your active alerts in a clean list.\n\n"
        "<b>🗑️ Cancel All</b>\n"
        "Delete all alert.\n\n"
        "<b>🔥 Trends</b>\n"
        "See currently trending cryptocurrencies and their live prices.\n\n"
        "⚙️ <b>Start / Restart</b>\n"
        "Use /start to restart the bot if needed.\n\n"
        "❓ Need help?\n"
        "Feel free to press help button anytime or contact the developer."
    )