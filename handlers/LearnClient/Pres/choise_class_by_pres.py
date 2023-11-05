from aiogram import types

from loader import dp
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class_button = [
	[KeyboardButton(text='7p')],
	[KeyboardButton(text='8p')],
	[KeyboardButton(text='9p')],
	[KeyboardButton(text='10p')],
	[KeyboardButton(text='11p')],
	[KeyboardButton(text='Выйти к выбору способов')],
]


@dp.message(lambda message: message.text == 'Презентации')
async def agree(message : types.Message):
    '''---CHOICE CLASS FOR USER IN EDUCATION---'''
    keyboard = ReplyKeyboardMarkup(keyboard=[*class_button],resize_keyboard = True)
    await message.reply('Выберите свой класс', reply = False, reply_markup=keyboard)