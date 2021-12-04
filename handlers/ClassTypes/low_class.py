from aiogram import types
from aiogram.dispatcher.filters.builtin import Text
from loader import dp


array_choice = [
					'7.1',
					'7.2',
					'7.3',
					'Выход'
				   ]


@dp.message_handler(Text(equals = '7 класс'))
async def choice(message : types.Message):
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
	keyboard.add(*array_choice)
	await message.reply('Темы:\n7.1 - Взаимодействие тел\n7.2 - Давление твёрдых тел, жидкостей и газов\n7.3 - Работа, энергия, мощность', reply = False)
	await message.reply('Выберите тему, из которой хотите узнать формулы 7 класса:',
		reply = False,
		reply_markup = keyboard)