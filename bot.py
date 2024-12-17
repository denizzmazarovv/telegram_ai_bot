import os
import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message

# Чтение токена из переменной окружения
TOKEN = os.getenv("BOT_TOKEN")

# Настройка логирования
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message_handler(commands=['start'])
async def send_welcome(message: Message):
    await message.reply("Добро пожаловать! Я ваш бот.")

# Новый способ запуска бота в aiogram 3.x
async def on_start():
    try:
        # Старт polling
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f"Error occurred: {e}")

if __name__ == "__main__":
    # Запуск с использованием asyncio.run для асинхронной функции
    asyncio.run(on_start())
