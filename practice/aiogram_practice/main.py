from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)

is_voted = False

ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('Like', callback_data='Like'), InlineKeyboardButton('Dislike', callback_data='Dislike')],
    [InlineKeyboardButton('Delete photo', callback_data='Remove')]
])


async def on_startup(_):
    print('Start bot')


@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    await bot.send_photo(message.from_user.id,
                         caption='Do you like it?',
                         photo='https://avatars.mds.yandex.net/i?id=fb3ba896392236a39cff328ec4db36c3bc2b5c2d-9106769-images-thumbs&n=13&exp=1',
                         reply_markup=ikb)


@dp.callback_query_handler(text='Remove')
async def close_callback(callback: types.CallbackQuery) -> None:
    global is_voted
    await callback.message.delete()
    is_voted = False


@dp.callback_query_handler()
async def bot_callback(callback: types.CallbackQuery):
    global is_voted
    if not is_voted:
        if callback.data == 'Like':
            await callback.answer(show_alert=True,
                                  text='You like it')
        else:
            await callback.answer(show_alert=True,
                                  text='You dislike it')
        is_voted = True
    else:
        await callback.answer('You already choose option')


if __name__ == '__main__':
    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=on_startup)
