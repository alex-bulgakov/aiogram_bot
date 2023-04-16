import hashlib

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from aiogram.utils.exceptions import BotBlocked
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent

from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)

storage = 0


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await message.answer('Enter num: ')


@dp.message_handler()
async def text_handler(message: types.Message) -> None:
    global storage
    storage = message.text
    await message.reply('Your data saved')


@dp.inline_handler()
async def inline_echo(inline_query: types.InlineQuery) -> None:
    global storage
    text = inline_query.query or 'echo'
    result_id: str = hashlib.md5(text.encode()).hexdigest()
    input_content = InputTextMessageContent(f'<b>{text}: </b>{storage}',
                                            parse_mode='HTML')

    item = InlineQueryResultArticle(
        id=result_id,
        input_message_content=input_content,
        title='Echo bot',
        description="I'm inline bot"
    )

    await bot.answer_inline_query(inline_query_id=inline_query.id,
                                  results=[item],
                                  cache_time=1)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
