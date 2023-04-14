from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from config import TOKEN


bot = Bot(TOKEN)
dp = Dispatcher(bot)

async def on_startup(_):
    print("I'm run")


kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton(text='/help')
b2 = KeyboardButton(text='/vote')
kb.add(b1, b2)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(message.chat.id,
                           text='Hello from bot',
                           reply_markup=kb)

@dp.message_handler(commands=['vote'])
async def vote_command(message: types.Message):
    ikb = InlineKeyboardMarkup(row_width=2)
    ib1 = InlineKeyboardButton(text='up',
                               callback_data="Yes")
    ib2 = InlineKeyboardButton(text='down',
                               callback_data="No")
    ikb.add(ib1,ib2)
    await bot.send_photo(   chat_id=message.from_user.id,
                            photo="https://cdn.citilink.ru/SiVDI5kBT_B6EPJ887PmSZ7YSTY2MT1_Pvf4NAOtPvM/resizing_type:fit/gravity:sm/width:1200/height:1200/plain/items/1913814_v01_b.jpg",
                            caption="Do you like it?",
                            reply_markup=ikb)

    await bot.send_message(chat_id=message.from_user.id,
                           text='Image')

@dp.callback_query_handler()
async def vote_callback(callback: types.CallbackQuery):
    if callback.data == 'Yes':
        await callback.answer(text='You like it')
    await callback.answer(text='You dislike it')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)