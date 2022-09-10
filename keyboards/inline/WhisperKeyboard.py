

from aiogram import types
from keyboards.inline import callback_data

from keyboards.inline.callback_data import whisper_callback


async def generate_button(id):
    button = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="Press button",
                    callback_data=whisper_callback.new(
                        msg_id = id
                    )
                )
            ]
        ]
    )

    return button