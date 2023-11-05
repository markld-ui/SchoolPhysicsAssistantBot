from aiogram import types
from handlers.filters.filters import TextFilter
from loader import dp
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


array_choice = [
    [KeyboardButton(text='10.1')],
    [KeyboardButton(text='10.2')],
    [KeyboardButton(text='10.3')],
    [KeyboardButton(text='Выход')],
]


@dp.message(TextFilter('10 класс'))
async def choice(message : types.Message):
	'''this function called to give themes in 10 class'''
	keyboard = ReplyKeyboardMarkup(keyboard=[*array_choice], resize_keyboard = True)
	await message.reply('Темы:\n10.1 - Механика\n10.2 - Молекулярная физика\n10.3 - Электродинамика за 10 класс', reply = False)
	await message.reply('Выберите тему, из которой хотите узнать формулы 10 класса:',
		reply = False,
		reply_markup = keyboard)