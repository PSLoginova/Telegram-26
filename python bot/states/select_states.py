from aiogram.dispatcher.filters.state import State, StatesGroup

class form_search(StatesGroup):
    waiting_for_level = State()  # Ожидание имени пользователя
    waiting_for_genre = State()   # Ожидание возраста пользователя
