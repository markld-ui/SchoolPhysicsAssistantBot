from aiogram import types

from loader import dp
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

choice_tems_eight_class = [
	[KeyboardButton(text='11.1p')],
	[KeyboardButton(text='11.2p')],
	[KeyboardButton(text='Выход к выбору P-класса')],
]


@dp.message(lambda message: message.text == '11p')
async def isPresForEight(message: types.Message):
	keyboard = ReplyKeyboardMarkup(keyboard=[*choice_tems_eight_class], resize_keyboard=True)

	await message.reply('Выберите тему, для которой хотите получить презентацию:', reply=False)
	await message.reply('Темы:\n11.1 - Электродинамика за 11 класс\n11.2 - Физика высоких энергий', reply=False, reply_markup=keyboard)