from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


b1 = KeyboardButton("Сhoice recipe")
b2 = KeyboardButton("Next, it's not tasty")
kb_client = ReplyKeyboardMarkup(resize_keyboard=True).add(b1)
kb_client2 = ReplyKeyboardMarkup(resize_keyboard=True).insert(b2)
