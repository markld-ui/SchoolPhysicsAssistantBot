from aiogram import types

from loader import dp


choice_tems_seven_class = [
		'7.1p',
		'7.2p',
		'7.3p', 
		'Выход к выбору P-класса'
]


@dp.message_handler(lambda message: message.text == '7p')
async def isPresForSeven(message: types.Message):
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.add(*choice_tems_seven_class)
	
	await message.reply('Выберите тему, для которой хотите получить презентацию:', reply=False)
	await message.reply('Темы:\n7.1p - Взаимодействие тел\n7.2p - Давление твёрдых тел, жидкостей и газов\n7.3p - Работа, энергия, мощность', reply=False, reply_markup=keyboard)