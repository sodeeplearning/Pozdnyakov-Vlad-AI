import asyncio
from aiogram import Bot, Dispatcher

import handlers
from config import bot_token


bot = Bot(token=bot_token)

dp = Dispatcher()
dp.include_router(handlers.router)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
