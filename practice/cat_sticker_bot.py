from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)
sticker_id = 'CAACAgIAAxkBAAICImQ4NC34oUUtEfkGokQJZZx_ux1sAALJCgAC3UeASt_0qcgKtqlpLwQ'
help = """
<b>/give</b> - Шлет кота
<b>/help</b> - Помощь
<b>✅ чекбоксы</b> - считает количество вхождений
<b>❤️ сердечки</b> - в ответ шлет черное сердечко - 🖤
"""


async def on_startup(_):
    print("Я запустился!")


@dp.message_handler(commands=['give'])
async def give_command(message: types.Message):
    await message.reply('Ля какой ржачный кот ' + '😀')
    await bot.send_sticker(message.from_user.id, sticker_id)
    message.delete()


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(help, parse_mode="HTML")
    await message.delete()


@dp.message_handler()
async def count_checkbox(message: types.Message):
    count = message.text.count('✅')
    await message.reply(count)


@dp.message_handler(content_types=types.ContentType.STICKER)
async def send_sticker_id(message: types.Message):
    global sticker_id
    await message.reply(f'The sticker ID is {sticker_id}')

@dp.message_handler()
async def send_blackHeart(message: types.Message):
    if message.text == '❤️':
        await message.reply('🖤')


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)
