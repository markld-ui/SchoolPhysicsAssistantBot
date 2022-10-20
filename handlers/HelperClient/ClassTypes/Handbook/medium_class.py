from aiogram import types
from aiogram.dispatcher.filters.builtin import Text
from loader import dp


array_choice = [
				'8.1',
				'8.2',
				'8.3',
				'8.4',
				'Выход'
				]


@dp.message_handler(Text(equals = '8 класс'))
async def choice(message : types.Message):
	'''this function called to give themes in 8 class'''
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
	keyboard.add(*array_choice)
	await message.reply('Темы:\n8.1 - Тепловые явления\n8.2 - Электрические явления\n8.3 - Электромагнитные явления\n8.4 - Световые явления', reply = False)
	await message.reply('Выберите тему, из которой хотите узнать формулы 8 класса:',
		reply = False,
		reply_markup = keyboard)