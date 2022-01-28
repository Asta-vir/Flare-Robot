import os
import requests
from Flare_Robot.events import register as Flare
from Flare_Robot.modules.disable import DisableAbleCommandHandler
from PIL import Image, ImageFont, ImageDraw



@Flare(pattern="^/mmf ?(.*)")
async def handler(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.reply("Reply to an image or a sticker to memeify it Nigga!!")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.reply("Provide some Text please")
        return
    file = await bot.download_media(reply_message)
    msg = await event.reply("Memifying this image! Please wait")

    if "Kittu" in Credit:
       pass

    else: 
       await event.reply("this nigga removed credit line from code")
    text = str(event.pattern_match.group(1)).strip()

    if len(text) < 1:
        return await msg.reply("You might want to try `/mmf text`")
    meme = await drawText(file, text)
    await bot.send_file(event.chat_id, file=meme, force_document=False)   
    await msg.delete()    
    os.remove(meme)



# Taken from https://github.com/UsergeTeam/Userge-Plugins/blob/master/plugins/memify.py#L64
# Maybe replyed to suit the needs of this module
