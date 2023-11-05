from aiogram import types

from loader import dp
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

choice_tems_eight_class = [
	[KeyboardButton(text='10.1p')],
	[KeyboardButton(text='10.2p')],
	[KeyboardButton(text='10.3p')],
	[KeyboardButton(text='Выход к выбору P-класса')],
]

@dp.message(lambda message: message.text == '10p')
async def isPresForEight(message: types.Message):
	keyboard = ReplyKeyboardMarkup(keyboard=[*choice_tems_eight_class], resize_keyboard=True)

	await message.reply('Выберите тему, для которой хотите получить презентацию:', reply=False)
	await message.reply('Темы:\n10.1 - Механика\n10.2 - Молекулярная физика\n10.3 - Электродинамика за 10 класс', reply=False, reply_markup=keyboard)