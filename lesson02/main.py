from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo_uppercase(msg: types.Message):
    await msg.answer(msg.text)

if __name__ == "__main__":
    executor.start_polling(dp)





