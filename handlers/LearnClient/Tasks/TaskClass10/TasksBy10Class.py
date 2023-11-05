from aiogram import types

from loader import dp
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


choice_tems_ten_class = [
	[KeyboardButton(text='10.1t')],
	[KeyboardButton(text='10.2t')],
	[KeyboardButton(text='10.3t')],
	[KeyboardButton(text='Выход к выбору T-класса')],
]

@dp.message(lambda message: message.text == '10t')
async def isPresForSeven(message: types.Message):
	keyboard = ReplyKeyboardMarkup(keyboard=[*choice_tems_ten_class], resize_keyboard=True)

	await message.reply('Выберите тему, для которой хотите получить задачи:', reply=False)
	await message.reply('Темы:\n10.1 - Механика\n10.2 - Молекулярная физика\n10.3 - Электродинамика за 10 класс', reply=False, reply_markup=keyboard)