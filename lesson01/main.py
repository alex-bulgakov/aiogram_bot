from aiogram import Bot, Dispatcher, executor, types

TOKEN = "1229443935:AAE-m94HuMj_F9a3IMlmK_04QA90oL5Zs1s"

bot = Bot(TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(text=message.text)

if __name__ == '__main__':
    executor.start_polling(dp)

