from aiogram import types

from loader import dp, bot

from handlers.LearnClient.Tasks.choise_class_by_tasks import class_button


@dp.message_handler(lambda message: message.text == '8.1t')
async def send_presentation_for_first_theme(message: types.Message):
    await message.answer('Задачи на тему "Тепловые явления"')
    await bot.send_chat_action(message.from_user.id, types.chat.ChatActions.UPLOAD_DOCUMENT)
    await message.reply_document(open('utils/media/Tasks/8class/8.1/tasks8_1.txt', 'rb'), reply=False)
    
    
@dp.message_handler(lambda message: message.text == '8.2t')
async def send_presentation_for_second_theme(message: types.Message):
    await message.answer('Задачи на тему "Электрические явления"')
    await bot.send_chat_action(message.from_user.id, types.chat.ChatActions.UPLOAD_DOCUMENT)
    await message.reply_document(open('utils/media/Tasks/8class/8.2/tasks8_2.txt', 'rb'), reply=False)
    

@dp.message_handler(lambda message: message.text == '8.3t')
async def send_presentation_for_third_theme(message: types.Message):
    await message.answer('Задачи на тему "Электромагнитные явления"')
    await bot.send_chat_action(message.from_user.id, types.chat.ChatActions.UPLOAD_DOCUMENT)
    await message.reply_document(open('utils/media/Tasks/8class/8.3/tasks8_3.txt', 'rb'), reply=False)
    
    
@dp.message_handler(lambda message: message.text == '8.4t')
async def send_presentation_for_third_theme(message: types.Message):
    await message.answer('Задачи на тему "Световые явления"')
    await bot.send_chat_action(message.from_user.id, types.chat.ChatActions.UPLOAD_DOCUMENT)
    await message.reply_document(open('utils/media/Tasks/8class/8.4/tasks8_4.txt', 'rb'), reply=False)
    

@dp.message_handler(lambda message: message.text == 'Выход к выбору T-класса')
async def exit_to_choice_p_class(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*class_button)
    await message.reply('Выберите свой класс', reply=False, reply_markup=keyboard)