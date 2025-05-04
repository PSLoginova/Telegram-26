from data.random_books import *
from aiogram import types, Dispatcher
from keyboards import *

async def process_random_book(call: types.CallbackQuery):
        data = call.data
        #print(f"Callback received: {callback_query.data}")  # Логирование данных callback

        # Получаем случайную книгу
        book = get_random_book()

        # Проверяем, что книга существует
        await call.message.answer(
            f"📚 {book['title']} — {book['desc']}\n"
            f"Уровень: {book['level']}, жанр: {book['genre']}",
        reply_markup=back())

def register_handlers_random_inline(dp: Dispatcher):
    dp.register_callback_query_handler(process_random_book, lambda call: call.data == "random_book")
