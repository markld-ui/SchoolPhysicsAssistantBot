from aiogram import types
from aiogram.dispatcher.filters.builtin import Text
from loader import dp


array_choice = [
					'Взаимодействие тел',
					'Давление твёрдых тел, жидкостей и газов',
					'Работа, энергия, мощность',
					'Выход'
				   ]


@dp.message_handler(Text(equals = '7 класс'))
async def choice(message : types.Message):
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard = False)
	keyboard.add(*array_choice)
	await message.reply('Выберите тему, из которой хотите узнать формулы 7 класса:',
		reply = False,
		reply_markup = keyboard)