import os

from telethon import Button, events

from userbot import *
from userbot.Config import Config
from userbot.plugins import *

ROYAL_IMG = os.environ.get(
    "BOT_PING_PIC", "https://telegra.ph/file/b4c7082f2c22283d66394.jpg"
)
ms = 4
ALIVE = Config.ALIVE_NAME

RoyalBoy = f"**⚡Ping⚡**\n\n   ⚜ {ms}\n   ⚜ ❝𝐌𝐲 𝐌𝐚𝐬𝐭𝐞𝐫❞ ~『{ALIVE}』"


@tgbot.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    GOOD = [[Button.url("ALFROZEN USERBOT", "https://t.me/ALFROZEN")]]
    await tgbot.send_file(event.chat_id, ROYAL_IMG, caption=RoyalBoy, buttons=GOOD)
