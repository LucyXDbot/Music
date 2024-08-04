from pyrogram import filters
from pyrogram.types import *
from AnonXMusic import app
from gpytranslate import Translator

#.......

trans = Translator()

#......

@app.on_message(filters.command("tr"))
async def translate(_, message) -> None:
    reply_msg = message.reply_to_message
    if not reply_msg:
        await message.reply_text("✦ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴛʀᴀɴsʟᴀᴛᴇ ɪᴛ !")
        return
    if reply_msg.caption:
        to_translate = reply_msg.caption
    elif reply_msg.text:
        to_translate = reply_msg.text
    try:
        args = message.text.split()[1].lower()
        if "//" in args:
            source = args.split("//")[0]
            dest = args.split("//")[1]
        else:
            source = await trans.detect(to_translate)
            dest = args
    except IndexError:
        source = await trans.detect(to_translate)
        dest = "en"
    translation = await trans(to_translate, sourcelang=source, targetlang=dest)
    reply = (
        f"✦ ᴛʀᴀɴsʟᴀᴛᴇᴅ ғʀᴏᴍ {source} ᴛᴏ {dest} ➥\n\n"
        f"♥︎ {translation.text}\n\n𖣐 ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥ ʟ ᴜ ᴄ ʏ • / ‹𝟹"
    )
    await message.reply_text(reply)
  
