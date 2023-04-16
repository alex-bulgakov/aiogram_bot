import hashlib

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from aiogram.utils.exceptions import BotBlocked
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent

from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.inline_handler()
async def inline_echo(inline_query: types.InlineQuery) -> None:
    text = inline_query.query or 'echo'
    input_content = InputTextMessageContent(text)
    result_id = hashlib.md5(text.encode()).hexdigest()

    item = InlineQueryResultArticle(
        input_message_content=input_content,
        id=result_id,
        title='echO'
    )

    await bot.answer_inline_query(inline_query_id=inline_query.id,
                                  results=[item],
                                  cache_time=1)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
