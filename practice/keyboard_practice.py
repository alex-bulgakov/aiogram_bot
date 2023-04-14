import random

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)
HELP_COMMENT = """
<b>/start</b> - start bot
<b>/help</b> - list of commands
<b>/description</b> - description of bot
"""
kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/description')
b3 = KeyboardButton('😀')
b4 = KeyboardButton('/sendphoto')
b5 = KeyboardButton('/random_location')
kb.add(b1,b2).add(b3, b4).add(b5)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(message.chat.id,
                           'welcome',
                           reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['random_location'])
async def random_location_command(message: types.Message):
    latitude = random.randint(-90, 90)
    longitude = random.randint(-180, 180)
    await bot.send_location(message.chat.id, latitude=latitude, longitude=longitude, horizontal_accuracy=0)
    await message.answer(str(latitude) + " " + str(longitude))


@dp.message_handler(commands=['sendphoto'])
async def sendphoto_command(message: types.Message):
    await bot.send_photo(message.chat.id, 'https://avatars.mds.yandex.net/i?id=3cdb2841ba80e3e517b421dd2e4fe9d2c4585cc6-9137660-images-thumbs&n=13&exp=1')


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(message.from_user.id, HELP_COMMENT,
                           parse_mode="HTML")
    await message.delete()


@dp.message_handler(commands=['description'])
async def descr_command(message: types.Message):
    await bot.send_message(message.from_user.id, "I can some")
    await message.delete()


@dp.message_handler()
async def reply_message(message: types.Message):
    if message.text == '😀':
        await bot.send_sticker(message.from_user.id,
                               sticker='CAACAgIAAxkBAAICTWQ4WFufThVbCxIjigEr3xcfMLRoAAI9DAAC70wRSn94XJTFnf7uLwQ')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
