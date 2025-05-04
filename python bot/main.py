from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import API_TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from handlers import start, help, recommend,inline_book_random, random_book, search_inline
from admin import register_admin
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton 

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Регистрируем хендлеры
inline_book_random.register_handlers_random_inline(dp)
search_inline.register_handlers_select_inline(dp)
# start.register_handlers_start(dp)
help.register_handlers_help(dp)
recommend.register_handlers_recommend(dp)
random_book.register_handlers_random(dp)
register_admin(dp)

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    # Создать клавиатуру прямо здесь
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton(text="🔍 Найти книгу", callback_data="find_book"),
        InlineKeyboardButton(text="🎲 Случайная книга", callback_data="random_book"),
        InlineKeyboardButton(text="ℹ️ Помощь", callback_data="help")
    )
    await message.answer(
        "Привет! Я помогу тебе найти интересные книги на английском языке. Используй следующие команды:\n/help, /recommend, /random_book",
        reply_markup=keyboard        # Использовать тестовую клавиатуру
    )


if __name__ == "__main__":
    executor.start_polling(dp, allowed_updates=all)
