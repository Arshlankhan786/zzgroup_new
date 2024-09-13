# (c) github - @IllegalDeveloper ,telegram - https://telegram.me/illegal_Developer
# removing credits doesn't make you coder 

# special thanks @AbirHasan2005

import asyncio
import requests
import string
import random
from configs import Config
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait
from handlers.helpers import str_to_b64

async def reply_forward(message: Message, file_id: int):
    try:
        await message.reply_text(
            f"Files Will Be Deleted In 2 Minutes To Avoid Copyright Issues. Please Forward And Save Them.",
            disable_web_page_preview=True,
            quote=True
        )
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await reply_forward(message, file_id)

async def media_forward(bot: Client, user_id: int, file_id: int):
    try:
        if Config.SAVE_TO_GALLERY is True:
            return await bot.copy_message(chat_id=user_id, from_chat_id=Config.DB_CHANNEL,
                                          message_id=file_id, reply_markup=InlineKeyboardMarkup(
                                                [
                                                    [
                                                        InlineKeyboardButton("ᴡᴀᴛᴄʜ ᴏɴʟɪɴᴇ 👀 / ꜰᴀsᴛ ᴅᴏᴡɴʟᴏᴀᴅ 🗂️", callback_data="stream")
                                                    ]
                                                ]
                                            )
                                         )
        elif Config.SAVE_TO_GALLERY is False:
            return await bot.copy_message(chat_id=user_id, from_chat_id=Config.DB_CHANNEL,
                                          message_id=file_id, reply_markup=InlineKeyboardMarkup(
                                                [
                                                    [
                                                        InlineKeyboardButton("ᴡᴀᴛᴄʜ ᴏɴʟɪɴᴇ 👀 / ꜰᴀsᴛ ᴅᴏᴡɴʟᴏᴀᴅ 🗂️", callback_data="stream")
                                                    ]
                                                ]
                                            ),
                                         protect_content=True)
            
    except FloodWait as e:
        await asyncio.sleep(e.value)
        return media_forward(bot, user_id, file_id)
        await message.delete()

async def send_media_and_reply(bot: Client, user_id: int, file_id: int):
    sent_message = await media_forward(bot, user_id, file_id)
    await reply_forward(message=sent_message, file_id=file_id)
    asyncio.create_task(delete_after_delay(sent_message, 120))

async def delete_after_delay(message, delay):
    await asyncio.sleep(delay)
    await message.delete()
