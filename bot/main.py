import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties
from bot.config import load_config
from bot.handlers import register_all_handlers
from database.models import create_tables
from utils.scheduler import check_alerts

logging.basicConfig(level=logging.INFO)

async def main():
    create_tables()
    config = load_config()

    bot = Bot(token=config.bot_token.get_secret_value(),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML,))

    dp = Dispatcher(storage=MemoryStorage())

    register_all_handlers(dp)

    asyncio.create_task(check_alerts(bot))

    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Stop.")