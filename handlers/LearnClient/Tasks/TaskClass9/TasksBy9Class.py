from aiogram import types

from loader import dp


choice_tems_nine_class = [
		'9.1t',
		'9.2t',
		'9.3t', 
		'Выход к выбору T-класса'
]


@dp.message_handler(lambda message: message.text == '9t')
async def isPresForSeven(message: types.Message):
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.add(*choice_tems_nine_class)
	
	await message.reply('Выберите тему, для которой хотите получить задачи:', reply=False)
	await message.reply('Темы:\n9.1 - Законы взаимодействия и движения тел\n9.2 - Электромагнитное поле\n9.3 - Строение атома и атомного ядра', reply=False, reply_markup=keyboard)