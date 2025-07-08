from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="➕ Set Up"),] ,
        [KeyboardButton(text="👁 View Alerts")],
        [KeyboardButton(text="❌ Cancel All"), KeyboardButton(text="📈 Market Trends")],
        [KeyboardButton(text="🚀 Top Gainers"), KeyboardButton(text="🔻 Top Losers")],
        [KeyboardButton(text="💰 Check Price"), KeyboardButton(text="ℹ️ Help")]
    ],
    resize_keyboard=True
)