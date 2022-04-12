from aiogram import types
from loader import dp


@dp.message_handler(lambda message: message.text == 'Кем разработан этот проект?')
async def disagree(message: types.Message):
    array_disagree = [
                        'Да',
                        'Нет'
                     ]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(*array_disagree)
    await message.reply('Этот проект находится в стадии разработки. Пока что над ним работает ученик МАОУ СОШ 197 г. Екатеринбург 10 класса.',
        reply = False)
    await message.reply('Перейдём к выбору опции?',
        reply = False,
        reply_markup = keyboard)