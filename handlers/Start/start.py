from aiogram import types

from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


'''---START COMMAND---'''

@dp.message_handler(CommandStart())
async def start(message : types.Message):
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True) #resize_keyboard - аргумент, регулирующий размер кнопочной клавиатуры
	frist_buttons = ['Да, конечно', 'Расскажи о себе'] #Создаем список кнопок
	keyboard.add(*frist_buttons) #Добавляем кнопки из списка
	await message.reply('Привет!\n'
                        'Я твой персональный бот-помощник по физике.\n'
                        'Начнём?',
                        reply = False, #Запрещаем боту отвечать на наше сообщение
                        reply_markup=keyboard #Выходными данными метода reply класса message будет являться кнопочная клавиатура
                        )