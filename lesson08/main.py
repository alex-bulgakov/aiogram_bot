from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)
HELP_COMMENT = """
<b>/help</b> - list of commands
<b>/start</b> - start bot
<b>/description</b> - description of bot
<b>/photo</b> - show photo
"""
kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/photo')
b3 = KeyboardButton('/description')
kb.add(b1).add(b2, b3)

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(message.from_user.id, HELP_COMMENT,
                           parse_mode="HTML")
    await message.delete()


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Welcome!',
                           reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['description'])
async def descr_command(message: types.Message):
    await bot.send_message(message.from_user.id, "I can send photos")
    await message.delete()


@dp.message_handler(commands=['photo'])
async def photo_command(message: types.Message):
    await bot.send_message(message.from_user.id, "https://hlopotyshki.ru/wp-content/uploads/2022/04/chisti-chetverg-17.jpg")
    await message.delete()



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
