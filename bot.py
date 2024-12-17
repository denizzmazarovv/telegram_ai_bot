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
from aiogram import Bot, Dispatcher, types
import logging
import asyncio
from aiogram.types import Message
from aiogram.contrib.middlewares.logging import LoggingMiddleware

# Чтение токена из конфигурации
TOKEN = os.getenv("BOT_TOKEN")  # Токен должен быть в переменной окружения или в config.json

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Создание экземпляра бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Добавление middleware для логирования
dp.middleware.setup(LoggingMiddleware())

# Обработчик команды /start
@dp.message_handler(commands=["start"])
async def send_welcome(message: Message):
    await message.reply("Добро пожаловать! Я ваш бот-консультант.")

# Обработчик текстовых сообщений
@dp.message_handler()
async def echo(message: Message):
    await message.answer(f"Вы написали: {message.text}")

# Новый способ запуска бота в aiogram 3.x
async def on_start():
    try:
        # Старт polling
        await dp.start_polling()
    except Exception as e:
        logger.error(f"Error occurred: {e}")

if __name__ == "__main__":
    # Запуск с использованием asyncio.run для асинхронной функции
    asyncio.run(on_start())
