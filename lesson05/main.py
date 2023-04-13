from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)
sticker_id = ''

async def on_startup(_):
    print('on_startup function')


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('Start bot - <b>COOL BOT</b>', parse_mode="HTML")


@dp.message_handler(content_types=types.ContentType.STICKER)
async def send_sticker_id(message: types.Message):
    global sticker_id
    sticker_id = message.sticker.file_id
    await message.reply(f'The sticker ID is {sticker_id}')

@dp.message_handler(commands=['give'])
async def give_command(message: types.Message):
    await bot.send_sticker(message.from_user.id, sticker=sticker_id)

@dp.message_handler()
async def send_emojy(message: types.Message):
    await message.reply(message.text + '😀')

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)
