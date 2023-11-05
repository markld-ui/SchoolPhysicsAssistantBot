from aiogram import types

from loader import dp
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


choice_tems_eight_class = [
	[KeyboardButton(text='9.1p')],
	[KeyboardButton(text='9.2p')],
	[KeyboardButton(text='9.3p')],
	[KeyboardButton(text='Выход к выбору P-класса')],
]



@dp.message(lambda message: message.text == '9p')
async def isPresForEight(message: types.Message):
	keyboard = ReplyKeyboardMarkup(keyboard=[*choice_tems_eight_class], resize_keyboard=True)

	await message.reply('Выберите тему, для которой хотите получить презентацию:', reply=False)
	await message.reply('Темы:\n9.1 - Законы взаимодействия и движения тел\n9.2 - Электромагнитное поле\n9.3 - Строение атома и атомного ядра', reply=False, reply_markup=keyboard)