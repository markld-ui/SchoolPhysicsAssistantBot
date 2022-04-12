from aiogram import types
from aiogram.dispatcher.filters.builtin import Text
from loader import dp


array_choice = [
				'11.1',
				'11.2',
				'Выход'
				]


@dp.message_handler(Text(equals = '11 класс'))
async def choice(message : types.Message):
	'''this function called to give themes in 11 class'''
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
	keyboard.add(*array_choice)
	await message.reply('Темы:\n11.1 - Электродинамика за 11 класс\n11.2 - Физика высоких энергий', reply = False)
	await message.reply('Выберите тему, из которой хотите узнать формулы 11 класса:',
		reply = False,
		reply_markup = keyboard)