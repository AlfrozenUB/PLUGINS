import time
from datetime import datetime
from io import BytesIO

import requests
from PIL import Image

from userbot import ALIVE_NAME, CmdHelp, ROYALversion
from userbot.__init__ import StartTime
from userbot.Config import Config, Vars

CUSTOM_ALIVE = (
    Var.CUSTOM_ALIVE_TEXT
    if Var.CUSTOM_ALIVE_TEXT
    else "༒︎ ᴀʟꜰʀᴏᴢᴇɴ ɪꜱ ᴀʟɪᴠᴇ ༒"
)
ROYAL_IMG = Var.ROYAL_IMG if Var.ROYAL_IMG else None
alivemoji = Var.CUSTOM_ALIVE_EMOJI if Var.CUSTOM_ALIVE_EMOJI else "🖤️"
if Config.SUDO_USERS:
    sudo = "Enabled"
else:
    sudo = "Disabled"


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


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "@AlfrozenX"


@bot.on(admin_cmd(outgoing=True, pattern="alive"))
@bot.on(sudo_cmd(outgoing=True, pattern="alive", allow_sudo=True))
async def ifiamalive(alive):
    start = datetime.now()
    myid = bot.uid
    """ For .alive command, check if the bot is running.  """
    end = datetime.now()
    (end - start).microseconds / 1000
    uptime = get_readable_time((time.time() - StartTime))
    if ALV_PIC:
        ROYAL_caption  = f"**🖤 ᴛʜᴇ ᴀʟꜰʀᴏᴢᴇɴ ᴜꜱᴇʀʙᴏᴛ 🖤️**\n\n"
        ROYAL_caption  += f"`{CUSTOM_ALIVE}`\n\n"
        ROYAL_caption  += f"┏━━━━━━━━━━━━━━━━━━━\n"
        ROYAL_caption  += (
            f"┣➣ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ**: `1.17`\n┣➣ **ᴘʏᴛʜᴏɴ**: `3.9.2`\n"
        )
        ROYAL_caption  += f"┣➣ ** ᴀʟꜰʀᴏᴢᴇɴ ᴠᴇʀsɪᴏɴ**: `{ROYALversion}`\n"
        ROYAL_caption  += f"┣➣ **ᴊᴏɪɴ**: @ErinaSupport\n"
        ROYAL_caption  += f"┣➣ **sᴜᴅᴏ** : `{sudo}`\n"
        ROYAL_caption  += f"┣➣ **ᴍʏ ɢʀᴏᴜᴘ**: `{CUSTOM_YOUR_GROUP}`\n"
        )
        ROYAL_caption += f"┗━━━━━━━━━━━━━━━━━━━\n"
        ROYAL_caption += "[ʀᴇᴘᴏ](https://github.com/AlfrozenUB/AlfrozenUB)"
        await alive.get_chat()
        await alive.delete()
        """ For .alive command, check if the bot is running.  """
        await borg.send_file(alive.chat_id, ALV_PIC, caption=ROYAL_caption , link_preview=False)
        await alive.delete()
        return
    req = requests.get("https://telegra.ph/file/5aca70b99835227e170a0.jpg")
    req.raise_for_status()
    file = BytesIO(req.content)
    file.seek(0)
    img = Image.open(file)
    with BytesIO() as sticker:
        img.save(sticker, "webp")
        sticker.name = "sticker.webp"
        sticker.seek(0)
        await borg.send_message(
            alive.chat_id,
            f"**🖤 𝗧𝗵𝗲 𝗔𝗹𝗳𝗿𝗼𝘇𝗲𝗻 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 🖤️**\n\n"
            f"`{Config.ALIVE_MSG}`\n\n"
            f"┏━━━━━━━━━━━━━━━━━━━\n"
            f"┣➣ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ**: `1.17`\n┣➣ **ᴘʏᴛʜᴏɴ**: `3.9.2`\n"
            f"┣➣ **ᴀʟꜰʀᴏᴢᴇɴ ᴜꜱᴇʀʙᴏᴛ ᴠᴇʀsɪᴏɴ**: `{rizoelversion}`\n"
            f"┣➣ **ᴊᴏɪɴ**: @ErinaSUpport\n"
            f"┣➣ **sᴜᴅᴏ** : `{sudo}`\n"
            f"┣➣ **ᴜᴘᴛɪᴍᴇ**: `{uptime}`\n"
            f"┣➣ __master__   : {mention}\n"
            f"┗━━━━━━━━━━━━━━━━━━━\n\n"
            f"[ʀᴇᴘᴏ](https://github.com/AlfrozenUserbot/Rizoeluserbot)",
            link_preview=False,
        )
        await borg.send_file(alive.chat_id, file=sticker)
        await alive.delete()


CmdHelp.update({"alive": "➨ `.alive`\nUse - Check is it Alive or Dead(RIP)."})
