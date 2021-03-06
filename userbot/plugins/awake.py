import time

from telethon import version

from ROYALBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot import ROYALversion, StartTime
from userbot.cmdhelp import CmdHelp

from . import *


async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO_USERS:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id


ROYAL_IMG = Config.AWAKE_PIC
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG or "Royals Choice ROYALBOT"
CUSTOM_YOUR_GROUP = Config.YOUR_GROUP or "@ANimeCHatGRoup"


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - StartTime))


@bot.on(admin_cmd(outgoing=True, pattern="awake$"))
@bot.on(sudo_cmd(pattern="awake$", allow_sudo=True))
async def amireallyalive(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)

    if ROYAL_IMG:
        ROYAL_caption = f"**{royal_mention}**\n"

        ROYAL_caption += f"~~~~~~~~~~~~~~~~~~~~~~~\n"
        ROYAL_caption += f"     β ROYALBOT IS AWAKE β\n"
        ROYAL_caption += f"β’π₯β’ ALFROZEN USERBOT     : Ξ½1.0\n"
        ROYAL_caption += f"β’π₯β’ ππ΄π»π΄ππ·πΎπ½      : `{version.__version__}`\n"
        ROYAL_caption += f"β’π₯β’ ππΏππΈπΌπ΄         : `{uptime}`\n"
        ROYAL_caption += f"β’π₯β’ π²π·π°π½π½π΄π»        : [π?Π½Ξ±ΠΈΠΈΡβ](t.me/ALFROZEN)\n"
        ROYAL_caption += f"β’π₯β’ α΄ΉΚΈ πΆππΎππΏ : {CUSTOM_YOUR_GROUP}\n"

        await event.client.send_file(
            event.chat_id, ROYAL_IMG, caption=ROYAL_caption, reply_to=reply_to_id
        )
        await event.delete()
    else:
        await edit_or_reply(
            awake,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"~~~~~~~~~~~~~~~~~~~~~~~ \n"
            f"         π­ππ πΎπππππ\n"
            f"β’β‘β’ πΏΡβΡΟΠ½ΞΏΠΈ    : `{version.__version__}`\n"
            f"π?π³ ALFROZEN BOT  : `{ROYALversion}`\n"
            f"π?π³ ΟΟΟΞΉΠΌΡ        : `{uptime}`\n"
            f"π± Ι±Ξ±ΰΈ£Ζ­Ξ΅ΙΎ        : {mention}\n"
            f"π± ΟΟΙ³Ξ΅ΙΎ         : [ROYAL](t.me/MRELLIOTALDERSON)\n",
        )


CmdHelp("awake").add_command("awake", None, "ΟΡΡ Ξ±ΠΈβ ΡΡΡ").add_info(
    "Same Like Alive"
).add_type("Official").add()
