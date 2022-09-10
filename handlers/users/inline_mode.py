import sqlite3

import uuid

from aiogram import types
from aiogram.types import message

from loader import dp, db

from keyboards.inline.WhisperKeyboard import generate_button

@dp.inline_handler()
async def empty_query(query: types.InlineQuery):


    text = query.query
    
    lst = text.split("||")

    txt_len = len(text)

    if len(lst) >= 2:
        as_len = len(lst[1])
    else:
        as_len = 0

    if len(lst) >= 2 and txt_len<=255 and as_len<200:

        #print(text)
        msg_id = str(uuid.uuid4())


        #Xabarni ba'zaga qo'shamiz
        db.add_message(
            message_id = msg_id,
            message_text = text,
            name = query.from_user.full_name,
            user_id = query.from_user.id,
            tg_username = query.from_user.username 
        )

        button = await generate_button(msg_id)



        result = types.InlineQueryResultArticle(
            id=msg_id,
            title=f"Whisper Message | {len(lst[1])}/200 | {txt_len}/255",
            input_message_content=types.InputTextMessageContent(
                message_text="New message",
            ),
            reply_markup=button,
        )

        await query.answer(results=[result,])
    else:


        result = types.InlineQueryResultArticle(
            id=str(uuid.uuid4()),
            title=f"Yaroqsiz Xabar | {as_len}/200 | {txt_len}/255",
            input_message_content=types.InputTextMessageContent(
                message_text="New message",
            )
        )

        await query.answer(results=[result,])
    
