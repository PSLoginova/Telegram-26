from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def back():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton(text="Вернуться Назад", callback_data="back")
    )
    return keyboard

def select_level():
    keyboard = InlineKeyboardMarkup(row_width=3)
    keyboard.add(
        InlineKeyboardButton(text="A1", callback_data="A1"),
        InlineKeyboardButton(text="A2", callback_data="A2"),
        InlineKeyboardButton(text="B1", callback_data="B1"),
        InlineKeyboardButton(text="B2", callback_data="B2"),
        InlineKeyboardButton(text="C1", callback_data="C1")
    )
    return keyboard

def select_genre():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("Adventure", callback_data="adventure"),
        InlineKeyboardButton("Detective", callback_data="detective"),
        InlineKeyboardButton("Science fiction", callback_data="science_fiction"),
        InlineKeyboardButton("Historical fiction", callback_data="historical_fiction"),
        InlineKeyboardButton("Fantasy", callback_data="fantasy"),
        InlineKeyboardButton("Romance novel", callback_data="romance_novel"),
        InlineKeyboardButton("Short stories", callback_data="short_stories"),
        InlineKeyboardButton("Western", callback_data="western"),
        InlineKeyboardButton("Horror", callback_data="horror"),
        InlineKeyboardButton("Classic", callback_data="classic")
    )
    return keyboard