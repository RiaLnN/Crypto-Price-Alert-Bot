from aiogram import Router, types
from aiogram.filters import CommandStart
from bot.keyboards.menu import main_menu

start_router = Router()



@start_router.message(CommandStart())
async def cmd_start(message: types.Message):
    user = message.from_user
    await message.answer(f"Welcome {user.full_name}! Choose an action below 👇", reply_markup=main_menu)