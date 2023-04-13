from aiogram import Bot, Dispatcher, executor, types

with open("../config.py") as f:
    TOKEN = f.readline().strip()


bot = Bot(TOKEN)

dp = Dispatcher(bot)


@dp.message_handler()
async def echo_uppercase(msg: types.Message):
    if len(msg.text.split(" ")) > 2:
        await msg.answer(msg.text)

if __name__ == "__main__":
    executor.start_polling(dp)





