from aiogram import types

from loader import dp
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


choice_tems_eight_class = [
	[KeyboardButton(text='8.1t')],
	[KeyboardButton(text='8.2t')],
	[KeyboardButton(text='8.3t')],
	[KeyboardButton(text='8.4t')],
	[KeyboardButton(text='Выход к выбору T-класса')],
]


@dp.message(lambda message: message.text == '8t')
async def isPresForSeven(message: types.Message):
	keyboard = ReplyKeyboardMarkup(keyboard=[*choice_tems_eight_class],resize_keyboard=True)

	await message.reply('Выберите тему, для которой хотите получить задачи:', reply=False)
	await message.reply('Темы:\n8.1 - Тепловые явления\n8.2 - Электрические явления\n8.3 - Электромагнитные явления\n8.4 - Световые явления', reply=False, reply_markup=keyboard)