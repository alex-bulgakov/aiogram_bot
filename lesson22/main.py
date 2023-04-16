from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import TOKEN

ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('Like', callback_data='like'), InlineKeyboardButton('Dislike', callback_data='dislike')]
])

bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message) -> None:
    await message.answer('photo', reply_markup=ikb)


@dp.callback_query_handler()
async def ikb_callback(callback: types.callback_query):
    if callback.data == 'like':
        await callback.answer('you liked it')
    else:
        await callback.answer('you dislike it')



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)