from aiogram import types
from loader import dp
from handlers.HelperClient.ClassTypes.Handbook.medium_class import array_choice
from handlers.HelperClient.ClassTypes.choice_class import class_button
from loader import bot


@dp.message_handler(lambda message: message.text == '8.1')
async def formuls(message : types.Message):
    '''function for 8.1 theme'''
    media = types.MediaGroup()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(*array_choice)
    await message.reply(
    'Вами выбрана тема "Тепловые явления". Пожалуйста: ',
    reply = False,
    reply_markup = keyboard)
    media.attach_photo(types.InputFile('utils\\media\\image\\8class\\teplovieyavleniyap1.jpg'))
    media.attach_photo(types.InputFile('utils\\media\\image\\8class\\teplovieyavleniyap2.jpg'))
    await bot.send_chat_action(message.from_user.id, types.chat.ChatActions.UPLOAD_PHOTO)
    await bot.send_media_group(message.chat.id, media=media)


@dp.message_handler(lambda message: message.text == '8.2')
async def formuls(message : types.Message):
    '''function for 8.2 theme'''
    media = types.MediaGroup()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(*array_choice)
    await message.reply(
    'Вами выбрана тема "Электрические явления". Пожалуйста: ',
    reply = False,
    reply_markup = keyboard)
    media.attach_photo(types.InputFile('utils\\media\\image\\8class\\electricheskieyavleniyap1.jpg'))
    media.attach_photo(types.InputFile('utils\\media\\image\\8class\\electricheskieyavleniyap2.jpg'))
    await bot.send_chat_action(message.from_user.id, types.chat.ChatActions.UPLOAD_PHOTO)
    await bot.send_media_group(message.chat.id, media=media)


@dp.message_handler(lambda message: message.text == '8.3')
async def formuls(message : types.Message):
    '''function for 8.3 theme'''
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(*array_choice)
    await message.reply(
    'Вами выбрана тема "Электромагнитные явления". Пожалуйста: ',
    reply = False,
    reply_markup = keyboard)
    await bot.send_chat_action(message.from_user.id, types.chat.ChatActions.UPLOAD_PHOTO)
    await bot.send_photo(chat_id = message.chat.id, photo = open('utils\\media\\image\\8class\\electromagnitnieyavleniya.jpg', 'rb'))


@dp.message_handler(lambda message: message.text == '8.4')
async def formuls(message : types.Message):
    '''function for 8.4 theme'''
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(*array_choice)
    await message.reply(
    'Вами выбрана тема "Световые явления". Пожалуйста: ',
    reply = False,
    reply_markup = keyboard)
    await bot.send_chat_action(message.from_user.id, types.chat.ChatActions.UPLOAD_PHOTO)
    await bot.send_photo(chat_id = message.chat.id, photo = open('utils\\media\\image\\8class\\svetovieyacleniya.jpg', 'rb'))


@dp.message_handler(lambda message: message.text == 'Выход')
async def exit(message: types.Message):
    '''function for exit in choice class'''
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(*class_button)
    await message.reply(
    'Выберите класс, в котором хотите посмотреть новые формулы:',
    reply = False,
    reply_markup = keyboard
    )