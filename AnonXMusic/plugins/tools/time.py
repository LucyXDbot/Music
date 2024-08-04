from pyrogram import Client, filters
from datetime import datetime
import pytz
from AnonXMusic import app
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


EVAA = [
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/nykaaxbot?startgroup=true"),
    ],
]


def get_current_time():
    tz = pytz.timezone('Asia/Kolkata')  # Setting the timezone to India (Kolkata)
    current_time = datetime.now(tz)
    return current_time.strftime("%Y-%m-%d %H:%M:%S %Z%z")

@app.on_message(filters.command(["Time"]))
def send_time(client, message):
    time = get_current_time()
    client.send_message(message.chat.id, f"𖣐 ᴄᴜʀʀʀɴᴛ ᴛɪᴍᴇ ᴏғ ɪɴᴅɪᴀ ⏤͟͟͞͞★\n\n● {time}", caption=f"𖣐 ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥ ʟ ᴜ ᴄ ʏ • / ‹𝟹", reply_markup=InlineKeyboardMarkup(EVAA),)
  
