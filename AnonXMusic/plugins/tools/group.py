from pyrogram import Client, filters
from pyrogram.types import Message
from AnonXMusic import app
from config import OWNER_ID



@app.on_message(filters.video_chat_started)
async def brah(_, msg):
       await msg.reply("𖣐 ᴠᴏɪᴄᴇ ᴄʜᴀᴛ sᴛᴀʀᴛᴇᴅ ᴏɴ ᴛʜɪs ɢʀᴏᴜᴘ.")


@app.on_message(filters.video_chat_ended)
async def brah2(_, msg):
       await msg.reply("𖣐 ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴇɴᴅᴇᴅ ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ.")




####

@app.on_message(filters.command("math", prefixes="/"))
def calculate_math(client, message):   
    expression = message.text.split("/math ", 1)[1]
    try:        
        result = eval(expression)
        response = f"𖣐 ᴛʜᴇ ʀᴇsᴜʟᴛ ɪs ➥ {result}"
    except:
        response = "𖣐 ɪɴᴠᴀʟɪᴅ ᴇxᴘʀᴇssɪᴏɴ"
    message.reply(response)

###
@app.on_message(filters.command("leavegroup")& filters.user(OWNER_ID))
async def bot_leave(_, message):
    chat_id = message.chat.id
    text = f"𖣐 ʙᴏᴛ sᴜᴄᴄᴇssғᴜʟʟʏ ʟᴇғᴛ ᴛʜᴇ ɢʀᴏᴜᴘ."
    await message.reply_text(text)
    await app.leave_chat(chat_id=chat_id, delete=True)

