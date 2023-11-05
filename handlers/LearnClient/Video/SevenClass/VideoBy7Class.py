from aiogram import types

from loader import dp

arrayWithThemes = ['7.1v', '7.2v', '7.3v', 'Выйти к выбору V-класса']

@dp.message_handler(lambda message: message.text == '7v')
async def isVideoForSeven(message: types.Message):
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard= True)
	keyboard.add(*arrayWithThemes)
	await message.reply('Выберите тему, для которой хотите получить видео:', reply=False)
	await message.reply('Темы:\n7.1 - Взаимодействие тел\n7.2 - Давление твёрдых тел, жидкостей и газов\n7.3 - Работа, энергия, мощность', reply=False, reply_markup=keyboard)