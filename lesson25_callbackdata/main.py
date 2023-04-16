from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)

cb = CallbackData('ikb', 'action')

ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('btn', callback_data=cb.new('push'))]
])


@dp.callback_query_handler(cb.filter())
async def ikb_callback(callback: types.CallbackQuery, callback_data: dict) -> None:
    if callback_data['action'] == 'push':
        await callback.answer('some')


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer('some text', reply_markup=ikb)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
