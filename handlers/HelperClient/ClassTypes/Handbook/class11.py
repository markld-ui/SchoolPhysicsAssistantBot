from aiogram import types
from handlers.filters.filters import TextFilter
from loader import dp
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


array_choice = [
    [KeyboardButton(text='11.1')],
    [KeyboardButton(text='11.2')],
    [KeyboardButton(text='Выход')],
]


@dp.message(TextFilter('11 класс'))
async def choice(message : types.Message):
	'''this function called to give themes in 11 class'''
	keyboard = ReplyKeyboardMarkup(keyboard=array_choice, resize_keyboard = True)
	await message.reply('Темы:\n11.1 - Электродинамика за 11 класс\n11.2 - Физика высоких энергий', reply = False)
	await message.reply('Выберите тему, из которой хотите узнать формулы 11 класса:',
		reply = False,
		reply_markup = keyboard)