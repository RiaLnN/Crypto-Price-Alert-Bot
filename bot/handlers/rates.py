import httpx
from aiogram import Router, types, F

rates_router = Router()

@rates_router.message(F.text == '🚀 Top Gainers')
async def show_top_gainers(message: types.Message):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 100,
        "page": 1,
        "price_change_percentage": "24h"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        data = response.json()

    sorted_data = sorted(
        data,
        key=lambda x: x.get("price_change_percentage_24h", 0),
        reverse=True
    )

    result = "🚀 *Top 10 Gainers in the last 24h:*\n\n\n"
    for i, coin in enumerate(sorted_data[:10], start=1):
        symbol = coin["symbol"].upper()
        change = round(coin.get("price_change_percentage_24h", 0), 2)
        result += f"{i}. {symbol} 🔼 +{change}%\n\n"

    await message.answer(result, parse_mode="Markdown")

@rates_router.message(F.text == '🔻 Top Losers')
async def show_top_losers(message: types.Message):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 100,
        "page": 1,
        "price_change_percentage": "24h"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        data = response.json()

    sorted_data = sorted(
        data,
        key=lambda x: x.get("price_change_percentage_24h", 0),
        reverse=False
    )

    result = "📉 *Top 10 losers in the last 24h:*\n\n\n"
    for i, coin in enumerate(sorted_data[:10], start=1):
        symbol = coin["symbol"].upper()
        change = round(coin.get("price_change_percentage_24h", 0), 2)
        result += f"{i}. {symbol} 🔻 {change}%\n\n"

    await message.answer(result, parse_mode="Markdown")
