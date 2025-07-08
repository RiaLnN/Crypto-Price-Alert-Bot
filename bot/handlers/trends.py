from aiogram import types, Router, F
from bot.services.crypto_api import get_trending_cryptos

trends_router = Router()



@trends_router.message(F.text == '📈 Market Trends')
async def cmd_trends(message: types.Message):
    cryptos = await get_trending_cryptos()
    if not cryptos:
        await message.answer("🚫 Failed to fetch trending coins. Try again later.")
        return
    text = "<b>🔥 Top Trending Cryptocurrencies:</b>\n\n\n"
    for coin in cryptos:
        text += f"• {coin['name']} ({coin['symbol']}) — <code>${coin['price']}</code>\n\n"

    await message.answer(text)
