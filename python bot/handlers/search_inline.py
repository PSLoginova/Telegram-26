from aiogram import types, Dispatcher
from keyboards import *
from aiogram.dispatcher import FSMContext
from states.select_states import *
from data.books import books


async def process_help2(call: types.CallbackQuery, state: FSMContext):
    data = call.data
    await call.message.answer(
        "Выберете ваш уровень английского:",
    reply_markup=select_level())
    await state.set_state(form_search.waiting_for_level)

async def process_help3(call: types.CallbackQuery, state: FSMContext):
    data = call.data
    print(data[-1])
    
    int(data[-1])
    await state.update_data(level=data)
    await call.message.answer(
        "Выберете ваш жанр который вам интересен:",
    reply_markup=select_genre())
    await state.set_state(form_search.waiting_for_genre)

async def process_help4(call: types.CallbackQuery, state: FSMContext):
    info = await state.get_data()
    level = info["level"]
    genre = call.data
    try:
        if level in books and genre in books[level]:
            recs = books[level][genre]
            response = f"Вот несколько книг уровня {level} в жанре {genre}:\n\n"
            for b in recs:
                response += f"📖 {b['title']} — {b['desc']}\n"
            await call.message.answer(f"{response}", reply_markup=back())
        else:
            await call.message.answer("Извините, я не нашёл книги по этим критериям. Попробуйте другой уровень или жанр.")
    except:
        pass
    await state.finish()

async def back_menu(call: types.CallbackQuery, state:FSMContext):
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton(text="🔍 Найти книгу", callback_data="find_book"),
        InlineKeyboardButton(text="🎲 Случайная книга", callback_data="random_book"),
        InlineKeyboardButton(text="ℹ️ Помощь", callback_data="help")
    )
    await call.message.answer(
        "Я помогу тебе найти интересные книги на английском языке. Используй следующие команды:\n/help, /recommend, /random_book",
        reply_markup=keyboard        # Использовать тестовую клавиатуру
    )
    await state.finish()



def register_handlers_select_inline(dp: Dispatcher):
    dp.register_callback_query_handler(process_help2, lambda call: call.data == "find_book")
    dp.register_callback_query_handler(process_help3, state=form_search.waiting_for_level)
    dp.register_callback_query_handler(process_help4, state=form_search.waiting_for_genre)
    dp.register_callback_query_handler(back_menu, lambda call: call.data == "back")