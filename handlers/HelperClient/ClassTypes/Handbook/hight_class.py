from aiogram import types
from aiogram.dispatcher.filters.builtin import Text
from loader import dp


array_choice = [
				'9.1',
				'9.2',
				'9.3',
				'Выход'
				]


@dp.message_handler(Text(equals = '9 класс'))
async def choice(message : types.Message):
	'''this function called to give themes in 9 class'''
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
	keyboard.add(*array_choice)
	await message.reply('Темы:\n9.1 - Законы взаимодействия и движения тел\n9.2 - Электромагнитное поле\n9.3 - Строение атома и атомного ядра', reply = False)
	await message.reply('Выберите тему, из которой хотите узнать формулы 9 класса:',
		reply = False,
		reply_markup = keyboard)