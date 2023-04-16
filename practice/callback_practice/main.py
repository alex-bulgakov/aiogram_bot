import random

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)
n = 0


def get_inline_keyboard() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('+', callback_data='btn_+'), InlineKeyboardButton('-', callback_data='btn_-')],
        [InlineKeyboardButton('random number', callback_data='btn_random')]

    ])
    return ikb


@dp.message_handler(commands='start')
async def start_command(message: types.Message) -> None:
    await message.answer(f'Counter: {n}',
                         reply_markup=get_inline_keyboard())


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('btn'))
async def count_callback(callback: types.CallbackQuery) -> None:
    global n
    if callback.data == 'btn_+':
        n += 1
    elif callback.data == 'btn_-':
        n -= 1
    elif callback.data == 'btn_random':
        await callback.message.edit_text(str(random.randint(0, 999)), reply_markup=get_inline_keyboard())
        return
    await callback.message.edit_text(str(n), reply_markup=get_inline_keyboard())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
