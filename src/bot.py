import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from dotenv import load_dotenv
import asyncio

load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(commands=["start"])
async def send_welcome(message: Message):
    await message.answer("👋 Привет! Это стартовое сообщение от OTC ELF бота.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
