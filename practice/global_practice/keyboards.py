from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

#main menu
kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton(text='/start')
b2 = KeyboardButton(text='/help')
b3 = KeyboardButton(text='/description')
b4 = KeyboardButton(text='/photomenu')
b5 = KeyboardButton(text='/getemoji')
b6 = KeyboardButton(text='/getsticker')
b7 = KeyboardButton(text='/getrandomlocation')
kb.add(b1, b2, b3).add(b5, b6, b7).add(b4)

#photo menu
kb2 = ReplyKeyboardMarkup(resize_keyboard=True)
bb1 = KeyboardButton(text='/getphoto')
bb2 = KeyboardButton(text='/mainmenu')
kb2.add(bb1, bb2)

#inline photo keyboard
ikb = InlineKeyboardMarkup(row_width=3)
like_btn = InlineKeyboardButton(text='Like', callback_data='Like')
dislike_btn = InlineKeyboardButton(text='Dislike', callback_data='Dislike')
next_btn = InlineKeyboardButton(text='Next', callback_data='Next')
ikb.add(next_btn, like_btn, dislike_btn)
