import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher

from app.handlers import router


bot = Bot(token='7172611579:AAF3vGXidt5BBgGRSxPNff5Lj4D0DkEHJxg')


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
