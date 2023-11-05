from aiogram import types
from handlers.filters.filters import TextFilter
from loader import dp
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


array_choice = [
    [KeyboardButton(text='8.1')],
    [KeyboardButton(text='8.2')],
    [KeyboardButton(text='8.3')],
    [KeyboardButton(text='8.4')],
    [KeyboardButton(text='Выход')],
]


@dp.message(TextFilter('8 класс'))
async def choice(message : types.Message):
	'''this function called to give themes in 8 class'''
	keyboard = ReplyKeyboardMarkup(keyboard=[*array_choice], resize_keyboard = True)
	await message.reply('Темы:\n8.1 - Тепловые явления\n8.2 - Электрические явления\n8.3 - Электромагнитные явления\n8.4 - Световые явления', reply = False)
	await message.reply('Выберите тему, из которой хотите узнать формулы 8 класса:',
		reply = False,
		reply_markup = keyboard)