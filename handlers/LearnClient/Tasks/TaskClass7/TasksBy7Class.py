from aiogram import types

from loader import dp


choice_tems_seven_class = [
		'7.1t',
		'7.2t',
		'7.3t', 
		'Выход к выбору T-класса'
]


@dp.message_handler(lambda message: message.text == '7t')
async def isPresForSeven(message: types.Message):
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.add(*choice_tems_seven_class)
	
	await message.reply('Выберите тему, для которой хотите получить задачи:', reply=False)
	await message.reply('Темы:\n7.1t - Взаимодействие тел\n7.2t - Давление твёрдых тел, жидкостей и газов\n7.3t - Работа, энергия, мощность', reply=False, reply_markup=keyboard)