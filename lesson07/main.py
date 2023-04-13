from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)
HELP_COMMENT = """
<b>/start</b> - <em>start bot</em>
<b>/help</b> - <em>help me</em>
<b>/image</b> - <em>help me</em>
"""

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    # await message.answer(message.text)
    # await bot.send_message(chat_id=message.from_user.id,
    #                  text=message.text)
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_COMMENT,
                           parse_mode="HTML")
    await message.delete()

@dp.message_handler(commands=['img'])
async def send_image(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo='https://hlopotyshki.ru/wp-content/uploads/2022/04/chisti-chetverg-17.jpg')
    await message.delete()


@dp.message_handler(commands=['locate'])
async def locate_command(message: types.Message):
    await bot.send_location(chat_id=message.chat.id,
                            latitude=0,
                            longitude=0)
    await message.delete()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
