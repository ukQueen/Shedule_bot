import asyncio
import logging
import sys
import os

from aiogram import Bot, Dispatcher
from app.handlers import router
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("token"))


async def main() -> None:
    # await bot.delete_webhook()
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        # asyncio.run(clear_schedule())
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")
