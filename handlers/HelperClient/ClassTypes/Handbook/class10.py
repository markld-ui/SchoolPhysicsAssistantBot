from aiogram import types
from aiogram.dispatcher.filters.builtin import Text
from loader import dp


array_choice = [
				'10.1',
				'10.2',
				'10.3',
				'Выход'
				]


@dp.message_handler(Text(equals = '10 класс'))
async def choice(message : types.Message):
	'''this function called to give themes in 10 class'''
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
	keyboard.add(*array_choice)
	await message.reply('Темы:\n10.1 - Механика\n10.2 - Молекулярная физика\n10.3 - Электродинамика за 10 класс', reply = False)
	await message.reply('Выберите тему, из которой хотите узнать формулы 10 класса:',
		reply = False,
		reply_markup = keyboard)