import asyncio

from ROYALBOT.utils import admin_cmd
from userbot import *
from userbot import ALIVE_NAME
from userbot.cmdhelp import CmdHelp

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ROYAL"


@borg.on(admin_cmd(pattern="independence$"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 6
    animation_ttl = range(0, 17)
    await event.edit("Starting...")
    animation_chars = [
        "**нєℓℓο!👋**",
        "**нοω αяє υ?**",
        f"**{DEFAULTUSER} : нαρργ ιи∂єρєи∂єиϲє ∂αγ**",
        "ωιѕнιиg υ нαρργ ιи∂єρєи∂єиϲє ∂αγ",
        "**Happy 😊 Indpendence Day!**",
        "**From every mountain side Let Fredom Ring**",
        "**Independence means.. enjoying freedom and empowering others too to let them do so.**",
        "ͲϴᎠᎪᎽ ᏔᎬ ᎪᎡᎬ ҒᎡᎬᎬ ᏴᎬᏟᎪႮՏᎬ ᎷᎪΝᎽ ՏᎪᏟᎡᏆҒᏆᏟᎬᎠ ͲᎻᎬᎡᎬ ᏞᏆᏙᎬՏ ҒϴᎡ ᏆΝᎠᏆᎪ \nՏᎪᏞႮͲᎬ ͲᎻᎬ ᏀᎡᎬᎪͲ ՏϴႮᏞՏ",
        "[ƒοя υ](https://telegra.ph/file/66205f168d8c2a0bbaa43.jpg)",
        "[нαρργ ιи∂ρєи∂єиϲє ∂αγ](https://t.me/BR_guild)",
    ]
    for i in animation_ttl:  # By @Samim3316 RoyalBot

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 17], link_preview=True)


CmdHelp("indpendence").add_command("independence", None, "Happy Indpendance Day").add()
