from aiogram import types

from loader import dp


choice_tems_eight_class = [
		'8.1p',
		'8.2p',
		'8.3p',
		'8.4p',
		'Выход к выбору P-класса'
]


@dp.message_handler(lambda message: message.text == '8p')
async def isPresForEight(message: types.Message):
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.add(*choice_tems_eight_class)
	
	await message.reply('Выберите тему, для которой хотите получить презентацию:', reply=False)
	await message.reply('Темы:\n8.1 - Тепловые явления\n8.2 - Электрические явления\n8.3 - Электромагнитные явления\n8.4 - Световые явления', reply=False, reply_markup=keyboard)