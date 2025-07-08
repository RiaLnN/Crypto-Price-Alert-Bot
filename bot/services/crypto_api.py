import httpx
import aiohttp
import matplotlib.pyplot as plt

from io import BytesIO
async def get_current_price(coin: str) -> float:
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        return data[coin]['usd']

async def get_trending_cryptos(limit: int = 5):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": limit,
        "page": 1,
        "sparkline": "false"
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            if response.status == 200:
                data = await response.json()
                return [
                    {
                        "name": coin["name"],
                        "symbol": coin["symbol"].upper(),
                        "price": coin["current_price"]
                    }
                    for coin in data
                ]
            else:
                return []


