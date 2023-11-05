from aiogram import types

from loader import dp
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


choice_tems_eight_class = [
	[KeyboardButton(text='8.1p')],
	[KeyboardButton(text='8.2p')],
	[KeyboardButton(text='8.3p')],
	[KeyboardButton(text='8.4p')],
	[KeyboardButton(text='Выход к выбору P-класса')],
]



@dp.message(lambda message: message.text == '8p')
async def isPresForEight(message: types.Message):
	keyboard = ReplyKeyboardMarkup(keyboard=[*choice_tems_eight_class], resize_keyboard=True)

	await message.reply('Выберите тему, для которой хотите получить презентацию:', reply=False)
	await message.reply('Темы:\n8.1 - Тепловые явления\n8.2 - Электрические явления\n8.3 - Электромагнитные явления\n8.4 - Световые явления', reply=False, reply_markup=keyboard)