from aiogram import types, Dispatcher
from keyboards import *

async def cmd_help(message: types.Message):
    await message.answer(
        "/start — запустить бота\n"
        "/help — инструкция по использованию\n"
        "/recommend <уровень> <жанр> — получить рекомендации\n"
        "/random_book — случайная книга на английском"
    )

async def process_help1(call: types.CallbackQuery):
    data = call.data
    await call.message.answer(
        "/start — запустить бота\n"
        "/help — инструкция по использованию\n"
        "/recommend <уровень> <жанр> — получить рекомендации\n"
        "/random_book — случайная книга на английском",
    reply_markup=back())

def register_handlers_help(dp: Dispatcher):
    dp.register_message_handler(cmd_help, commands=["help"])
    dp.register_callback_query_handler(process_help1, lambda call: call.data == "help")
