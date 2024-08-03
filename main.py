import os
import asyncio
import logging
from aiogram import Dispatcher, Bot
import commands
from handlers import messages
from database.connection import init_db

logging.basicConfig(level=logging.INFO)
key = os.getenv("KEY")
bot = Bot(key)
dp = Dispatcher()

dp.include_router(commands.router)
dp.include_router(messages.router)

async def main():
    await init_db()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
