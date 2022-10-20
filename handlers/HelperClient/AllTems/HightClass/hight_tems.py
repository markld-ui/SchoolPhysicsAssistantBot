from aiogram import types
from loader import dp
from handlers.HelperClient.ClassTypes.Handbook.hight_class import array_choice
from handlers.HelperClient.ClassTypes.choice_class import class_button
from loader import bot


@dp.message_handler(lambda message: message.text == '9.1')
async def formuls(message : types.Message):
    '''function for 9.1 theme'''
    media = types.MediaGroup()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(*array_choice)
    await message.reply(
    'Вами выбрана тема "Законы взаимодействия и движения тел". Пожалуйста: ',
    reply = False,
    reply_markup = keyboard)
    media.attach_photo(types.InputFile('utils\\media\\image\\9class\\zakonivzaimodeistviyaidvijeniyatelp1.jpg'))
    media.attach_photo(types.InputFile('utils\\media\\image\\9class\\zakonivzaimodeistviyaidvijeniyatelp2.jpg'))
    media.attach_photo(types.InputFile('utils\\media\\image\\9class\\zakonivzaimodeistviyaidvijeniyatelp3.jpg'))
    media.attach_photo(types.InputFile('utils\\media\\image\\9class\\zakonivzaimodeistviyaidvijeniyatelp4.jpg'))
    media.attach_photo(types.InputFile('utils\\media\\image\\9class\\zakonivzaimodeistviyaidvijeniyatelp5.jpg'))
    await bot.send_chat_action(message.from_user.id, types.chat.ChatActions.UPLOAD_PHOTO)
    await bot.send_media_group(message.chat.id, media = media)


@dp.message_handler(lambda message: message.text == '9.2')
async def formuls(message : types.Message):
    '''function for 9.2 theme'''
    media = types.MediaGroup()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(*array_choice)
    await message.reply(
    'Вами выбрана тема "Электромагнитное поле". Пожалуйста: ',
    reply = False,
    reply_markup = keyboard)
    media.attach_photo(types.InputFile('utils\\media\\image\\9class\\electromagnitnoepolep1.jpg'))
    media.attach_photo(types.InputFile('utils\\media\\image\\9class\\electromagnitnoepolep2.jpg'))
    media.attach_photo(types.InputFile('utils\\media\\image\\9class\\electromagnitnoepolep3.jpg'))
    media.attach_photo(types.InputFile('utils\\media\\image\\9class\\electromagnitnoepolep4.jpg'))
    await bot.send_chat_action(message.from_user.id, types.chat.ChatActions.UPLOAD_PHOTO)
    await bot.send_media_group(message.chat.id, media = media)

@dp.message_handler(lambda message: message.text == '9.3')
async def formuls(message : types.Message):
    '''function for 9.3 theme'''
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(*array_choice)
    await message.reply(
    'Вами выбрана тема "Строение атома и атомного ядра". Пожалуйста: ',
    reply = False,
    reply_markup = keyboard)
    await bot.send_chat_action(message.from_user.id, types.chat.ChatActions.UPLOAD_PHOTO)
    await bot.send_photo(chat_id = message.chat.id, photo = open('utils\\media\\image\\9class\\stroenieatomyadra.jpg', 'rb'))


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