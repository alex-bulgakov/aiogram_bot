from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import  InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)

ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='Button 1',
                           url='https://google.com')

ib2 = InlineKeyboardButton(text='Button 2',
                           url='https://ya.ru')

ikb.add(ib1, ib2)


@dp.message_handler(commands=['start'])
async def send_kb(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Inline keyboard',
                           reply_markup=ikb)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
