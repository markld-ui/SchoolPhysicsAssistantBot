from aiogram import types
from handlers.filters.filters import TextFilter
from loader import dp
from loader import dp
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


array_choice = [
    [KeyboardButton(text='9.1')],
    [KeyboardButton(text='9.2')],
    [KeyboardButton(text='9.3')],
    [KeyboardButton(text='Выход')],
]


@dp.message(TextFilter('9 класс'))
async def choice(message : types.Message):
	'''this function called to give themes in 9 class'''
	keyboard = ReplyKeyboardMarkup(keyboard=[*array_choice], resize_keyboard = True)
	await message.reply('Темы:\n9.1 - Законы взаимодействия и движения тел\n9.2 - Электромагнитное поле\n9.3 - Строение атома и атомного ядра', reply = False)
	await message.reply('Выберите тему, из которой хотите узнать формулы 9 класса:',
		reply = False,
		reply_markup = keyboard)