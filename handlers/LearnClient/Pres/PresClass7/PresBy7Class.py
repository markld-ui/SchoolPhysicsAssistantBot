from aiogram import types

from loader import dp
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

choice_tems_seven_class = [
	[KeyboardButton(text='7.1p')],
	[KeyboardButton(text='7.2p')],
	[KeyboardButton(text='7.3p')],
	[KeyboardButton(text='Выход к выбору P-класса')],
]


@dp.message(lambda message: message.text == '7p')
async def isPresForSeven(message: types.Message):
	keyboard = ReplyKeyboardMarkup(keyboard=[*choice_tems_seven_class], resize_keyboard=True)

	await message.reply('Выберите тему, для которой хотите получить презентацию:', reply=False)
	await message.reply('Темы:\n7.1p - Взаимодействие тел\n7.2p - Давление твёрдых тел, жидкостей и газов\n7.3p - Работа, энергия, мощность', reply=False, reply_markup=keyboard)