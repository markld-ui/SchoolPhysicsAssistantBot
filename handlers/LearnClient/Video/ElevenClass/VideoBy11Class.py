from aiogram import types

from loader import dp

arrayWithThemes = ['11.1v', '11.2v', 'Выйти к выбору V-класса']

@dp.message_handler(lambda message: message.text == '11v')
async def isVideoForSeven(message: types.Message):
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard= True)
	keyboard.add(*arrayWithThemes)
	await message.reply('Выберите тему, для которой хотите получить видео:', reply=False)
	await message.reply('Темы:\n11.1 - Электродинамика за 11 класс\n11.2 - Физика высоких энергий', reply=False, reply_markup=keyboard)