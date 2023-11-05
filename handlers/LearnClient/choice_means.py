from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import types

from loader import dp

types_button = [
    [KeyboardButton(text='Презентации')],
    [KeyboardButton(text='Задачи')],
    [KeyboardButton(text='Выйти к выбору операции')],
]


@dp.message(lambda message: message.text == 'Образование')
async def agree(message : types.Message):
    '''---CHOICE CLASS FOR USER IN EDUCATION---'''
    keyboard = ReplyKeyboardMarkup(keyboard=[*types_button], resize_keyboard = True)
    await message.reply('Чем хотите воспользоваться?', reply = False, reply_markup=keyboard)