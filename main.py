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

@bot.on_message(filters.command("start") & filters.incoming)
async def start(bot, message):
    Button = InlineKeyboardMarkup(
            [
                 [
                    InlineKeyboardMarkup("support", url="https://t.me/RoBotXSupport"),
                    InlineKeyboardMarkup("updates", url="https://t.me/RobotXupdates"),
                 ]
             ]
        )
    await message.reply_text(f"ʜɪɪ  {message.from_user.mention()}\n\n๏ I ᴀᴍ n Instagram reels/post downloader bot just send me any Instagram post link I will download it for uh !!", reply_markup=Button)
