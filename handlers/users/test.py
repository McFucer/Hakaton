from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import Message
from aiogram.types.web_app_info import WebAppInfo
from loader import dp, bot
from keyboards.inline.markups import test_uzb, test_ru


@dp.callback_query_handler(text='uzb')
async def uzb(call:types.CallbackQuery,state:FSMContext):
    await state.set_state('uzb')
    await call.message.answer("<b>Kasb yo'naltirish testini</b> o'tish uchun pastdagi tugmani bosing👇🏼",
                              reply_markup=test_uzb)

@dp.callback_query_handler(text='ru')
async def uzb(call:types.CallbackQuery,state:FSMContext):
    await state.set_state('ru')
    await call.message.answer("Что-бы пройти <b>Проф.Ориентационный тест</b> нажмите кнопку снизу👇🏼",
                              reply_markup=test_ru)


@dp.callback_query_handler(lambda c: c.data.startswith('web_app_data'))
async def handle_web_app_data(callback_query: types.CallbackQuery):
    # Extract the data sent from the web application
    web_app_data = callback_query.data[len('web_app_data') + 1:]

    print(callback_query)  # All information about the callback query
    print(web_app_data)  # The specific data sent from the web application

    # Send a message to the chat with the received information
    await bot.send_message(callback_query.message.chat.id,
                           f"Received information from the web application: {web_app_data}")

