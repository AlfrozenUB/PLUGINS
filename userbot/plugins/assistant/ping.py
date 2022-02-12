import os

from telethon import Button, events

from userbot import *
from userbot.Config import Config
from userbot.plugins import *

ROYAL_IMG = os.environ.get(
    "BOT_PING_PIC", "https://telegra.ph/file/a9f6a3c160977352dd595.jpg"
)
ms = 4
ALIVE = Config.ALIVE_NAME

RoyalBoy = f"**꧁•⊹٭Ping٭⊹•꧂**\n\n   ⚜ {ms}\n   ⚜ ❝𝐌𝐲 𝐌𝐚𝐬𝐭𝐞𝐫❞ ~『{ALIVE}』"


@tgbot.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    GOOD = [[Button.url("⚜ ROYAL USERBOT ⚜", "https://t.me/BR_guild")]]
    await tgbot.send_file(event.chat_id, ROYAL_IMG, caption=RoyalBoy, buttons=GOOD)
