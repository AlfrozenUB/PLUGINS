import asyncio

from ROYALBOT.utils import admin_cmd
from userbot.cmdhelp import CmdHelp
from userbot.Config import Config

from . import *

CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG
# animation Idea by @Samim3316 (op coder)
# Kang with credits else gay...
# alive.py for

edit_time = 12
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/b4c7082f2c22283d66394.jpg"
file2 = "https://telegra.ph/file/b4c7082f2c22283d66394.jpg"
file3 = "https://telegra.ph/file/b4c7082f2c22283d66394.jpg"
file4 = "https://telegra.ph/file/b4c7082f2c22283d66394.jpg"
file5 = "https://telegra.ph/file/b4c7082f2c22283d66394.jpg"
file6 = "https://telegra.ph/file/b4c7082f2c22283d66394.jpg"
file7 = "https://telegra.ph/file/b4c7082f2c22283d66394.jpg"
file8 = "https://telegra.ph/file/b4c7082f2c22283d66394.jpg"
file9 = "https://telegra.ph/file/b4c7082f2c22283d66394.jpg"
file10 = "https://te.legra.ph/file/d4a4ef913997298bb1530.jpg"
file11 = "https://telegra.ph/file/b4c7082f2c22283d66394.jpg"
""" =======================CONSTANTS====================== """
pm_caption = f"** {CUSTOM_ALIVE_TEXT}**\n"
pm_caption += f"**╭────────────**\n"
pm_caption += f"┣»»»『{royal_mention}』«««\n"
pm_caption += f"┣ ALfrozen Userbot ~ {ROYALversion}\n"
pm_caption += f"┣ Owner  ~ [C R E A T O R ](https://t.me/AlfrozenX)\n"
pm_caption += f"┣ SUPPORT ~ [-G𝖗ουρ-](https://t.me/ErinaSupport)\n"
pm_caption += f"┣ REPO   ~ [-Rєρο-](https://github.com/AlfrozenUB/AlfrozenUB)\n"
pm_caption += f"┣ Co-Owner ~ [GReninja](https://t.me/Greninja_369)\n"
pm_caption += f"┣ Helper ~ [ ACGC ](https://t.me/AcGc_01/)\n"
pm_caption += f"**╰────────────**\n"


@borg.on(admin_cmd(pattern=r"about"))
@borg.on(sudo_cmd(pattern="about$", allow_sudo=True))
async def amireallyalive(yes):
    await yes.get_chat()

    on = await borg.send_file(yes.chat_id, file=file1, caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2)

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file4)

    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file5)

    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file4)

    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file3)

    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file2)

    await asyncio.sleep(edit_time)
    ok8 = await borg.edit_message(yes.chat_id, ok7, file=file1)

    await asyncio.sleep(edit_time)
    ok9 = await borg.edit_message(yes.chat_id, ok8, file=file2)

    await asyncio.sleep(edit_time)
    ok10 = await borg.edit_message(yes.chat_id, ok9, file=file3)

    await asyncio.sleep(edit_time)
    ok11 = await borg.edit_message(yes.chat_id, ok10, file=file4)

    await asyncio.sleep(edit_time)
    ok12 = await borg.edit_message(yes.chat_id, ok11, file=file5)

    await asyncio.sleep(edit_time)
    ok13 = await borg.edit_message(yes.chat_id, ok12, file=file1)

    await alive.delete()

    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()


CmdHelp("about").add_command("about", None, "BEST alive command").add_warning(
    "Harmless Module✅"
).add_info("Just Like Alive But Changing Alwayd Pic").add_type("Official").add()
