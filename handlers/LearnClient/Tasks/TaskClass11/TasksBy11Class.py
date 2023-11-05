from aiogram import types

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import dp

choice_tems_eleven_class = [
	[KeyboardButton(text='11.1t')],
	[KeyboardButton(text='11.2t')],
	[KeyboardButton(text='Выход к выбору T-класса')],
]


@dp.message(lambda message: message.text == '11t')
async def isPresForSeven(message: types.Message):
	keyboard = ReplyKeyboardMarkup(keyboard=[*choice_tems_eleven_class], resize_keyboard=True)

	await message.reply('Выберите тему, для которой хотите получить задачи:', reply=False)
	await message.reply('Темы:\n11.1 - Электродинамика за 11 класс\n11.2 - Физика высоких энергий', reply=False, reply_markup=keyboard)