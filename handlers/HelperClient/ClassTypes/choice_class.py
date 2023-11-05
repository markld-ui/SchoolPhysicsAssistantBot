from aiogram import types
from loader import dp
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class_button = [
    [KeyboardButton(text='7 класс')],
    [KeyboardButton(text='8 класс')],
    [KeyboardButton(text='9 класс')],
    [KeyboardButton(text='10 класс')],
    [KeyboardButton(text='11 класс')],
    [KeyboardButton(text='Выйти к выбору операции')],
]


@dp.message(lambda message: message.text == 'Справочник')
async def agree(message : types.Message):
    '''---CHOICE CLASS FOR USER IN HANDBOOK---'''
    keyboard = ReplyKeyboardMarkup(keyboard=[*class_button],resize_keyboard = True)

    await message.reply('Выберите свой класс', reply = False, reply_markup=keyboard)