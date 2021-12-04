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
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
	keyboard.add(*array_choice)
	await message.reply('Темы:\n10.1 - Электродинамика за 10 класс\n10.2 - Механика\n10.3 - Молекулярная физика', reply = False)
	await message.reply('Выберите тему, из которой хотите узнать формулы 10 класса:',
		reply = False,
		reply_markup = keyboard)