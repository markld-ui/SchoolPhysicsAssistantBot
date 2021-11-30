from aiogram import types
from aiogram.dispatcher.filters.builtin import Text
from loader import dp


array_choice = [
				'Электродинамика 11 класс',
				'Физика высоких энергий',
				'Выход'
				]


@dp.message_handler(Text(equals = '11 класс'))
async def choice(message : types.Message):
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard = False)
	keyboard.add(*array_choice)
	await message.reply('Выберите тему, из которой хотите узнать формулы 11 класса:',
		reply = False,
		reply_markup = keyboard)