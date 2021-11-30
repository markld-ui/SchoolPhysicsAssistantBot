from aiogram import types
from aiogram.dispatcher.filters.builtin import Text
from loader import dp


array_choice = [
				'Электродинамика 10 класс',
				'Механика',
				'Молекулярная физика',
				'Выход'
				]


@dp.message_handler(Text(equals = '10 класс'))
async def choice(message : types.Message):
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard = False)
	keyboard.add(*array_choice)
	await message.reply('Выберите тему, из которой хотите узнать формулы 10 класса:',
		reply = False,
		reply_markup = keyboard)