from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import dp


class_button = [
	[KeyboardButton(text='7t')],
	[KeyboardButton(text='8t')],
	[KeyboardButton(text='9t')],
	[KeyboardButton(text='10t')],
	[KeyboardButton(text='11t')],
	[KeyboardButton(text='Выйти к выбору способов')]
]


@dp.message(lambda message: message.text == 'Задачи')
async def agree(message : types.Message):
    '''---CHOICE CLASS FOR USER IN EDUCATION---'''
    keyboard = ReplyKeyboardMarkup(keyboard=[*class_button], resize_keyboard = True)
    await message.reply('Выберите свой класс', reply = False, reply_markup=keyboard)