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
    result_id_bold: str = hashlib.md5((text + 'bold').encode()).hexdigest()
    result_id_italic: str = hashlib.md5((text + 'italic').encode()).hexdigest()
    input_content_bold = InputTextMessageContent(f'<b>{text}</b>',
                                                 parse_mode='HTML')

    input_content_italic = InputTextMessageContent(f'<i>{text}</i>',
                                                   parse_mode='HTML')

    bold = InlineQueryResultArticle(
        id=result_id_bold,
        input_message_content=input_content_bold,
        title='Bold',
        thumb_url='https://avatars.mds.yandex.net/i?id=b199f80fd30b2a153b5f09429e1646327ddb0513-8496275-images-thumbs&n=13&exp=1'
    )

    italic = InlineQueryResultArticle(
        id=result_id_italic,
        input_message_content=input_content_italic,
        title='Italic',
        thumb_url='https://avatars.mds.yandex.net/i?id=2dfe607fb7d5a911c44e920420c624fa-5581032-images-thumbs&n=13&exp=1'
    )

    await bot.answer_inline_query(inline_query_id=inline_query.id,
                                  results=[bold, italic],
                                  cache_time=1)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
