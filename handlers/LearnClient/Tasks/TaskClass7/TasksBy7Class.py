from aiogram import types

from loader import dp
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


choice_tems_seven_class = [
	[KeyboardButton(text='7.1t')],
	[KeyboardButton(text='7.2t')],
	[KeyboardButton(text='7.3t')],
	[KeyboardButton(text='Выход к выбору T-класса')],
]

@dp.message(lambda message: message.text == '7t')
async def isPresForSeven(message: types.Message):
	keyboard = ReplyKeyboardMarkup(keyboard=[*choice_tems_seven_class], resize_keyboard=True)

	await message.reply('Выберите тему, для которой хотите получить задачи:', reply=False)
	await message.reply('Темы:\n7.1t - Взаимодействие тел\n7.2t - Давление твёрдых тел, жидкостей и газов\n7.3t - Работа, энергия, мощность', reply=False, reply_markup=keyboard)