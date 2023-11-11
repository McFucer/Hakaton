from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo

lang = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="O'zbek tili🇺🇿",callback_data='uzb')
    ],
    [
        InlineKeyboardButton(text='Русский язык🇷🇺',callback_data='ru')
    ],
])

test_uzb = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="Kasb yo'naltirish testi", web_app=WebAppInfo(url='https://master--marvelous-pika-08cf9e.netlify.app/'))
    ]
])
test_ru = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="Проф ориентация", web_app=WebAppInfo(url='https://master--marvelous-pika-08cf9e.netlify.app/'))
    ]
])
