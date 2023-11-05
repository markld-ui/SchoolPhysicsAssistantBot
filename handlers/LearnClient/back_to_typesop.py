from aiogram import types
from aiogram.types import ReplyKeyboardMarkup
from handlers.LearnClient.choice_means import types_button
from loader import dp


@dp.message(lambda message: message.text == 'Выйти к выбору способов')
async def exit(message: types.Message):
    '''function for exit in choice class'''
    keyboard = ReplyKeyboardMarkup(keyboard=[*types_button],resize_keyboard = True)
    await message.reply(
    'Выберите нужный для Вас способ образования:',
    reply = False,
    reply_markup = keyboard
    )