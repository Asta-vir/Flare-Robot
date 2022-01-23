from telethon import events, Button, custom
import os
from Flare_Robot.events import register
from Flare_Robot import telethn as tbot
from Flare_Robot import telethn as tgbot


PHOTO = "https://telegra.ph/file/1cd6d62ef6e8843e6b1cb.jpg"


@register(pattern=("/alive"))
async def awake(event):
  FLARE = event.sender.first_name
  FLARE = "**♡ I,m ғʟᴀʀᴇ ʀᴏʙᴏᴛ 愛 ** \n\n"
  FLARE += "**♡ I'm Working With sᴇxʏ Speed**\n\n"
  FLARE += "**♡ ғʟᴀʀᴇ: LATEST Version**\n\n"
  FLARE += "**♡ My Creator: [ᴀsᴛᴀ](http://t.me/Chifuyu_Matsuno_Kun)\n\n"
  FLARE += "**♡ ᴀɴʏ ɪssᴜᴇs ᴄᴏɴᴛᴀᴄᴛ ʜᴇʀᴇ @Freia_Support **\n"
  FLARE += "**♡ ᴛʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ 💘💘💘**\n"

  BUTTON = [[Button.url("🚑 Support", "https://t.me/Freia_Support"), Button.url("📢 Updates", "https://t.me/Freia_Updates")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=FLARE,  buttons=BUTTON)


__mod_name__ = "Alive"
