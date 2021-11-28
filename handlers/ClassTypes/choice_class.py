from aiogram import types

from loader import dp

class_button = ['7 класс', '8 класс', '9 класс']

'''---CHOICE CLASS FOR USER---'''

@dp.message_handler(lambda message: message.text =='Да, конечно') #Проверка выбранной кнопки
async def agree(message : types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True) # one_time_keyboard метод при значении "True" будет скрывать кнопочное меню, при нажатии на кнопку
    keyboard.add(*class_button)
    await message.reply('Выберите свой класс', reply = False, reply_markup=keyboard) #Вывод текста