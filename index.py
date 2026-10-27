import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

BOT_TOKEN = "8814573991:AAEu2fT6T97dMUAInzqQtKYT0nQaf3WYWxQ"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Привет! 👋")


@dp.message(F.text)
async def any_text(message: Message):
    await message.answer("Привет! 👋")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
