from aiogram import types
from aiogram.dispatcher.filters.builtin import Text
from loader import dp


array_choice = [
				'Законы взаимодействия и движения тел',
				'Электромагнитное поле',
				'Строение атома и атомного ядра',
				'Выход'
				]


@dp.message_handler(Text(equals = '9 класс'))
async def choice(message : types.Message):
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard = False)
	keyboard.add(*array_choice)
	await message.reply('Выберите тему, из которой хотите узнать формулы 9 класса:',
		reply = False,
		reply_markup = keyboard)