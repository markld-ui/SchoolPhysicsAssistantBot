from aiogram import types

from loader import dp
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


choice_tems_nine_class = [
	[KeyboardButton(text='9.1t')],
	[KeyboardButton(text='9.2t')],
	[KeyboardButton(text='9.3t')],
	[KeyboardButton(text='Выход к выбору T-класса')],
]



@dp.message(lambda message: message.text == '9t')
async def isPresForSeven(message: types.Message):
	keyboard = ReplyKeyboardMarkup(keyboard=[*choice_tems_nine_class], resize_keyboard=True)

	await message.reply('Выберите тему, для которой хотите получить задачи:', reply=False)
	await message.reply('Темы:\n9.1 - Законы взаимодействия и движения тел\n9.2 - Электромагнитное поле\n9.3 - Строение атома и атомного ядра', reply=False, reply_markup=keyboard)