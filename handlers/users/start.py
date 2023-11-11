from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import Message
from aiogram.types.web_app_info import WebAppInfo
from loader import dp
from keyboards.inline.markups import lang

@dp.message_handler(commands='start')
async def start(msg:types.Message,state:FSMContext):
    await msg.answer('<b>Выберите язык:\nTil tanlang:</b>',reply_markup=lang)

