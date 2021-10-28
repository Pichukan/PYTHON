from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os


bot=Bot(token=os.getenv('TOKEN'))
dp=Dispatcher(bot)

async def on_startup(_):
    print('Бот выскочил в онлайн')

'''*******************КЛИЕНТСКАЯ ЧАСТЬ******************'''
@dp.message_handler(commands=['start','help'])
async def command_start(message:types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита')
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/Ocenka_PichBot')

@dp.message_handler(commands=['Режим_работы'])
async def pizza_open_command(message:types.Message):
    await bot.send_message(message.from_user.id, 'Вс-Птн с 9:00 до 18:30, Сб,Вс - выходной')
    #await message.delete()
    #await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/Ocenka_PichBot')

@dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message:types.Message):
    await bot.send_message(message.from_user.id, 'Ул. Пушкина, д. Колотушкина')
    #await message.delete()
    #await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/Ocenka_PichBot')





'''*******************АДМИНСКАЯ ЧАСТЬ*******************'''


'''*******************ОБЩАЯ ЧАСТЬ***********************'''




@dp.message_handler()
async def echo_send(message:types.Message):
    if message.text=='Привет':

        await message.answer('И тебе привет')                              #бот отвечает в чат
    #await message.reply(message.text)                               #бот отвечает в чат с упоминанием пользователя
    #await bot.send_message(message.from_user.id, message.text)       #бот отвечает в личку пользователю




executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

