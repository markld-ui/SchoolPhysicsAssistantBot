from aiogram import types

from loader import dp


choice_tems_eight_class = [
		'9.1p',
		'9.2p',
		'9.3p',
		'Выход к выбору P-класса'
]


@dp.message_handler(lambda message: message.text == '9p')
async def isPresForEight(message: types.Message):
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.add(*choice_tems_eight_class)
	
	await message.reply('Выберите тему, для которой хотите получить презентацию:', reply=False)
	await message.reply('Темы:\n9.1 - Законы взаимодействия и движения тел\n9.2 - Электромагнитное поле\n9.3 - Строение атома и атомного ядра', reply=False, reply_markup=keyboard)