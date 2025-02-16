import asyncio
from aiogram import Bot, Dispatcher

from config import bot_token


bot = Bot(token=bot_token)


async def main():
    import private_hanlers
    import handlers

    dp = Dispatcher()

    dp.include_router(private_hanlers.router)
    dp.include_router(handlers.router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
