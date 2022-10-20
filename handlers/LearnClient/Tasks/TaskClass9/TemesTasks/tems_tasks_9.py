from aiogram import types

from loader import dp, bot

from handlers.LearnClient.Tasks.choise_class_by_tasks import class_button


@dp.message_handler(lambda message: message.text == '9.1t')
async def send_presentation_for_first_theme(message: types.Message):
    await message.answer('Задачи на тему "Законы взаимодействия и движения тел"')
    await bot.send_chat_action(message.from_user.id, types.chat.ChatActions.UPLOAD_DOCUMENT)
    await message.reply_document(open('utils/media/Tasks/9class/9.1/tasks9_1.txt', 'rb'), reply=False)
    
    
@dp.message_handler(lambda message: message.text == '9.2t')
async def send_presentation_for_second_theme(message: types.Message):
    await message.answer('Задачи на тему "Электромагнитное поле"')
    await bot.send_chat_action(message.from_user.id, types.chat.ChatActions.UPLOAD_DOCUMENT)
    await message.reply_document(open('utils/media/Tasks/9class/9.2/tasks9_2.txt', 'rb'), reply=False)
    

@dp.message_handler(lambda message: message.text == '9.3t')
async def send_presentation_for_third_theme(message: types.Message):
    await message.answer('Задачи на тему "Строение атома и атомного ядра"')
    await bot.send_chat_action(message.from_user.id, types.chat.ChatActions.UPLOAD_DOCUMENT)
    await message.reply_document(open('utils/media/Tasks/9class/9.3/tasks9_3.txt', 'rb'), reply=False)
    

@dp.message_handler(lambda message: message.text == 'Выход к выбору T-класса')
async def exit_to_choice_p_class(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*class_button)
    await message.reply('Выберите свой класс', reply=False, reply_markup=keyboard)