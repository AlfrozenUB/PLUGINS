from telethon import version

from ROYALBOT.utils import *
from userbot import *
from userbot.cmdhelp import CmdHelp

# -------------------------------------------------------------------------------

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ROYAL"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

royal = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={royal})"


PM_IMG = "https://telegra.ph/file/b4c7082f2c22283d66394.jpg"
pm_caption = "**Alfrozen 𝙸𝚜 𝙾𝚗𝚕𝚒𝚗𝚎**\n\n"

pm_caption += f"**┏🔥The Alfrozen Userbot🔥┓**\n"
pm_caption += f"**┣🚀 𝙼𝚢 𝙼𝚊𝚜𝚝𝚎𝚛    : {mention}**\n"
pm_caption += f"**┣🚀 𝚃𝚎𝚕𝚎𝚝𝚑𝚘𝚗 : `{version.__version__}`**\n"
pm_caption += f"**┣🚀 Alfrozen UB : {ROYALversion}**\n"
pm_caption += f"**┣🚀 𝚂𝚞𝚍𝚘     : `{sudou}`**\n"
pm_caption += f"**┣🚀 𝙾𝚠𝚗𝚎𝚛     : [Elliot](https://t.me/MrElliotAlderson)**\n"
pm_caption += f"**┗[♦️𝙶𝚛𝚘𝚞𝚙♦️](https://t.me/ANimeChatAura)┛**\n"

pm_caption += "    [✨яєρο✨](https://github.com/Kajukatliii/AlfrozenUB) 🔹 [📜License📜](https://github.com/Kajukatliii/alfrozenUB/blob/master/LICENSE)"


@bot.on(admin_cmd(outgoing=True, pattern="bot$"))
@bot.on(sudo_cmd(pattern="bot$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()


CmdHelp("alv").add_command(
    "alive", None, "Check weather the bot is alive or not"
).add_command(
    "bot",
    None,
    "Check weather the bot is alive or not. In your custom Alive Pic and Alive Msg",
).add_warning(
    "Harmless Module"
).add_info(
    "Are u alive?"
).add_type(
    "Official"
).add()
