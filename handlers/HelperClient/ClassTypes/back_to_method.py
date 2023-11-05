from aiogram import types
from handlers.HelperClient.ClassTypes.choice_method import methods_button
from loader import dp

from aiogram.types import ReplyKeyboardMarkup


@dp.message(lambda message: message.text == 'Выйти к выбору операции')
async def exit(message: types.Message):
    '''function for exit in choice class'''
    keyboard = ReplyKeyboardMarkup(keyboard=[*methods_button], resize_keyboard = True)
    await message.reply(
    'Выберите нужную для Вас функцию:',
    reply = False,
    reply_markup = keyboard
    )