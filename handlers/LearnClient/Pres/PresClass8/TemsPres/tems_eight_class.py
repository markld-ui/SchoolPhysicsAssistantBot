from aiogram import types

from loader import dp, bot

from handlers.LearnClient.Pres.choise_class_by_pres import class_button


@dp.message_handler(lambda message: message.text == '8.1p')
async def send_presentation_for_first_theme(message: types.Message):
    await message.answer('Презентация на тему "Тепловые явления"')
    await bot.send_chat_action(message.from_user.id, types.chat.ChatActions.UPLOAD_DOCUMENT)
    await message.reply_document(open('utils/media/Presentations/8class/8.1/pres1.txt', 'rb'), reply=False)
    
    
@dp.message_handler(lambda message: message.text == '8.2p')
async def send_presentation_for_second_theme(message: types.Message):
    await message.answer('Презентация на тему "Электрические явления"')
    await bot.send_chat_action(message.from_user.id, types.chat.ChatActions.UPLOAD_DOCUMENT)
    await message.reply_document(open('utils/media/Presentations/8class/8.2/pres2.txt', 'rb'), reply=False)
    

@dp.message_handler(lambda message: message.text == '8.3p')
async def send_presentation_for_third_theme(message: types.Message):
    await message.answer('Презентация на тему "Электромагнитные явления"')
    await bot.send_chat_action(message.from_user.id, types.chat.ChatActions.UPLOAD_DOCUMENT)
    await message.reply_document(open('utils/media/Presentations/8class/8.3/pres3.txt', 'rb'), reply=False)
    
    
@dp.message_handler(lambda message: message.text == '8.4p')
async def send_presentation_for_four_theme(message: types.Message):
    await message.answer('Презентация на тему "Световые явления"')
    await bot.send_chat_action(message.from_user.id, types.chat.ChatActions.UPLOAD_DOCUMENT)
    await message.reply_document(open('utils/media/Presentations/8class/8.4/pres4.txt', 'rb'), reply=False)
    
    

@dp.message_handler(lambda message: message.text == 'Выход к выбору P-класса')
async def exit_to_choice_p_class(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*class_button)
    await message.reply('Выберите свой класс', reply=False, reply_markup=keyboard)