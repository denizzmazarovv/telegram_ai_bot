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
import json
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
from transformers import pipeline

# Загружаем токен из config.json
with open("config.json", "r") as config_file:
    config = json.load(config_file)
    TOKEN = config["token"]

# Инициализация бота
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Загружаем AI-модель для вопрос-ответ
qa_pipeline = pipeline("question-answering", model="bert-base-multilingual-cased")

# Контекст для модели (замени на информацию о магазине)
context = """
В нашем магазине доступны размеры S, M и L. 
Доставка осуществляется в течение 3 дней по городу. 
Оплата принимается картой или наличными при получении.
"""

# Обработка сообщений
@dp.message_handler()
async def handle_message(message: Message):
    user_question = message.text
    try:
        # Обработка вопроса с помощью AI-модели
        result = qa_pipeline(question=user_question, context=context)
        answer = result['answer']
        await message.reply(answer)
    except Exception as e:
        await message.reply("Извините, я не понял ваш вопрос. Попробуйте иначе.")

# Запуск бота
if __name__ == "__main__":
    print("Бот запущен...")
    executor.start_polling(dp, skip_updates=True)