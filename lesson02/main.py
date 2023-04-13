from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN

dp = Dispatcher(Bot(TOKEN))

HELP_COMMAND = """
/start - start bot
/help - command list
"""


@dp.message_handler(commands=['help'])
async def help_command(msg: types.Message):
    await msg.reply(HELP_COMMAND)


@dp.message_handler(commands=['start'])
async def start_command(msg: types.Message):
    await msg.answer(text='Bot started')
    await msg.delete()

if __name__ == "__main__":
    executor.start_polling(dp)





