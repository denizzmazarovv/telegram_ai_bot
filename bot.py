# from aiogram import Bot, Dispatcher, types
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
# from aiogram.utils import executor

# # Вставь сюда свой токен от BotFather
# TOKEN = "7197694845:AAHrF6OeDcNoWDdFghKch03cpigu2wQy2f8"

# bot = Bot(token=TOKEN)
# dp = Dispatcher(bot)

# # Команда /start
# @dp.message_handler(commands=["start"])
# async def start_command(message: types.Message):
#     # Создаём клавиатуру с кнопкой для запуска мини-приложения
#     keyboard = InlineKeyboardMarkup()
#     keyboard.add(
#         InlineKeyboardButton(
#             text="Открыть MiniApp",
#             web_app=WebAppInfo(url="http://127.0.0.1:5000/")  # URL твоего приложения
#         )
#     )
#     await message.answer("Нажми на кнопку, чтобы открыть MiniApp:", reply_markup=keyboard)

# if __name__ == "__main__":
#     executor.start_polling(dp)
# -------------------------------------------------------------------------------
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
import logging
import asyncio

# Чтение токена из переменной окружения
TOKEN = os.getenv("BOT_TOKEN")

# Настройка логирования
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: Message):
    await message.reply("Добро пожаловать! Я ваш бот.")

# Новый способ запуска бота в aiogram 3.x
async def on_start():
    try:
        # Старт polling
        await dp.start_polling()
    except Exception as e:
        logging.error(f"Error occurred: {e}")

if __name__ == "__main__":
    # Запуск с использованием asyncio.run для асинхронной функции
    asyncio.run(on_start())
