import string
from random import randint

from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN

dp = Dispatcher(Bot(TOKEN))
DESCR = "type any words and bot answer random symbol"
counter = 0


@dp.message_handler(commands=['description'])
async def description_command(msg: types.Message):
    global counter
    counter += 1
    await msg.answer(DESCR)


@dp.message_handler(commands=['count'])
async def count_command(msg: types.Message):
    global counter
    await msg.answer(counter)


@dp.message_handler()
async def help_command(msg: types.Message):
    global counter
    counter += 1
    text = msg.text
    await msg.reply(string.ascii_letters[randint(0, len(text))])
    if text.find('0') > -1:
        await msg.reply("YES")
    else:
        await msg.reply("NO")


if __name__ == "__main__":
    executor.start_polling(dp)
