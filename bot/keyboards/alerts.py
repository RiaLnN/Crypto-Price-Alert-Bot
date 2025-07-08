

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def alert_buttons(coin: str, price: float):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📈 View Price Now", callback_data=f"view_{coin}")],
        [InlineKeyboardButton(text="🔁 Update Price", callback_data=f"update_{coin}")],
        [InlineKeyboardButton(text="❌ Delete", callback_data=f"delete_{coin}_{price}")]
    ])


def delete_buttons():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Remove all alerts", callback_data="warning")]
    ])

#Future functions (Dont work)
def direction_buttons(coin: str):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔼 Alert when price goes ABOVE", callback_data=f"up_{coin}")],
        [InlineKeyboardButton(text="🔽 Alert when price goes BELOW", callback_data=f"down_{coin}")],
        [InlineKeyboardButton(text="❌ Cancel", callback_data=f"cancel_{coin}")]
    ])