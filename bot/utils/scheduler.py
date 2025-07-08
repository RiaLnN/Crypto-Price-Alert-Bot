
import asyncio
from bot.services.crypto_api import get_current_price
from bot.database.queries import get_all_alerts, remove_alert
from aiogram import Bot

async def check_alerts(bot: Bot):
    while True:
        alerts = await get_all_alerts()

        for user_id, coin, price in alerts:

            current = await get_current_price(coin)
            if current >= price:
                await bot.send_message(user_id, f"🚨 {coin.upper()} reached ${current}!")
                await remove_alert(user_id, coin, price)
        await asyncio.sleep(60 * 5)
