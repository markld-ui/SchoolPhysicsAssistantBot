from aiogram import types

from loader import dp

arrayWithThemes = ['9.1v', '9.2v', '9.3v', 'Выйти к выбору V-класса']

@dp.message_handler(lambda message: message.text == '9v')
async def isVideoForSeven(message: types.Message):
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard= True)
	keyboard.add(*arrayWithThemes)
	await message.reply('Выберите тему, для которой хотите получить видео:', reply=False)
	await message.reply('Темы:\n9.1 - Законы взаимодействия и движения тел\n9.2 - Электромагнитное поле\n9.3 - Строение атома и атомного ядра', reply=False, reply_markup=keyboard)