import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher

from app.handlers import router
from token import token

bot = Bot(token=token)


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
