from pyrogram import filters, Client 
import re,asyncio
from os import mkdir
from random import randint
from requests import get
import traceback
import wget,os,traceback
from pymongo import MongoClient
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters, Client, errors, enums
from pyrogram.errors import UserNotParticipant
from pyrogram.errors.exceptions.flood_420 import FloodWait
import bs4, requests, logging 
from config import API_ID, API_HASH, BOT_TOKEN, OWNER_ID, LOGGER_ID, SUB, MONGO_URI

client = MongoClient(MONGO_URI)
users = client['main']['users']
groups = client['main']['groups']

logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)
bot=Client(name="insta-bot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,)

@shiv.on_message(filters.command("start") & filters.incoming)
async def start(shiv, message):
    try:
        await shiv.get_chat_member(CHID, message.from_user.id)
        add_user(message.from_user.id)
        await message.reply_text(f"__Hey__ {message.from_user.mention()} !! 🌹\n\n**I am a Telegram bot ❤️**\n__using which you can download Instagram reels. ⚡__\n\n**Extra Features ~ 👾**\n__Using this you can also generate telegraph link of any pic ⚡__ \n\n**Click** /help __for more information about the commands 📒__\n\n**By © @ITZ_RaBBiTX ❤️**")
        await shiv.send_message(LOG_GROUP, f"{message.from_user.mention()} __just started the bot ✅__")
    except UserNotParticipant:
        key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• ᴄʜᴇᴄᴋ ᴀɢᴀɪɴ •", "chk")
                ]
            ]
        )
        await message.reply_text("**⚠️ ᴀᴄᴄᴇꜱꜱ ᴅᴇɴɪᴇᴅ ⚠️**\n\n__ᴩʟᴇᴀꜱᴇ ᴊᴏɪɴ @RaBBiTXUpdates ᴛᴏ ᴜꜱᴇ ᴍᴇ ɪꜰ yᴏᴜ ᴊᴏɪɴᴇᴅ ᴄʟɪᴄᴋ ᴄʜᴇᴄᴋ ᴀɢᴀɪɴ ʙᴜᴛᴛᴏɴ ᴛᴏ confirm__", reply_markup=key)
