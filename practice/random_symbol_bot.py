from random import randint

from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN

dp = Dispatcher(Bot(TOKEN))
DESCR = "type any words and bot answer random symbol"


@dp.message_handler(msg: types.Message)
async def help_command(msg: types.Message):
    await msg.reply(msg.text[randint(0, len(msg.text))]


@dp.message_handler(commands=['description'])
async def description_command(msg: types.Message):
    await msg.reply(DESCR)


if __name__ == "__main__":
    executor.start_polling(dp)





