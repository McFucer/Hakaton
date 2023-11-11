from aiogram import types

from loader import dp


# Echo bot
@dp.message_handler(state='uzb')
async def bot_echo(message: types.Message):
    await message.answer('Sizni tushunmayabman')

@dp.message_handler(state='ru')
async def bot_echo(message: types.Message):
    await message.answer('Не понимаю вас')

@dp.callback_query_handler(text='gag')
async def gag(call:types.CallbackQuery):
    await call.answer('GGVP,')