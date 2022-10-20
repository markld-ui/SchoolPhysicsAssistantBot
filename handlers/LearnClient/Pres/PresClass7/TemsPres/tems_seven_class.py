from aiogram import types

from loader import dp, bot

from handlers.LearnClient.Pres.choise_class_by_pres import class_button


@dp.message_handler(lambda message: message.text == '7.1p')
async def send_presentation_for_first_theme(message: types.Message):
    await message.answer('Презентация на тему "Взаимодействие тел"')
    await bot.send_chat_action(message.from_user.id, types.chat.ChatActions.UPLOAD_DOCUMENT)
    await message.reply_document(open('utils\\media\\Presentations\\7class\\7.1\\pres1.txt', 'rb'), reply=False)
    
    
@dp.message_handler(lambda message: message.text == '7.2p')
async def send_presentation_for_second_theme(message: types.Message):
    await message.answer('Презентация на тему "Давление твёрдых тел, жидкостей и газов"')
    await bot.send_chat_action(message.from_user.id, types.chat.ChatActions.UPLOAD_DOCUMENT)
    await message.reply_document(open('utils\\media\\Presentations\\7class\\7.2\\pres2.txt', 'rb'), reply=False)
    

@dp.message_handler(lambda message: message.text == '7.3p')
async def send_presentation_for_third_theme(message: types.Message):
    await message.answer('Презентация на тему "Работа, энергия, мощность"')
    await bot.send_chat_action(message.from_user.id, types.chat.ChatActions.UPLOAD_DOCUMENT)
    await message.reply_document(open('utils\\media\\Presentations\\7class\\7.3\\pres3.txt', 'rb'), reply=False)
    

@dp.message_handler(lambda message: message.text == 'Выход к выбору P-класса')
async def exit_to_choice_p_class(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*class_button)
    await message.reply('Выберите свой класс', reply=False, reply_markup=keyboard)