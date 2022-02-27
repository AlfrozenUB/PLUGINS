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
file1 = "https://te.legra.ph/file/8841e79cdf046b2b34cf4.mp4"
file2 = "https://telegra.ph/file/8b10cae7ca007a4d3b6fd.jpg"
file3 = "https://te.legra.ph/file/7351e8a4abe4777859775.jpg"
file4 = "https://te.legra.ph/file/9d7c6ea1e5ae5763c9033.jpg"
file5 = "https://te.legra.ph/file/ec5fb7bda2b1172149221.jpg"
file6 = "https://te.legra.ph/file/844a28a4fcfbc0de96da6.jpg"
file7 = "https://te.legra.ph/file/e8a5ed100a01d56573e58.jpg"
file8 = "https://te.legra.ph/file/1db8efca075b838417977.jpg"
file9 = "https://te.legra.ph/file/3da121b329b4483c57829.jpg"
file10 = "https://te.legra.ph/file/d4a4ef913997298bb1530.jpg"
file11 = "https://te.legra.ph/file/a8b74d9f6ff30b09e321a.jpg"
""" =======================CONSTANTS====================== """
pm_caption = f"** {CUSTOM_ALIVE_TEXT}**\n"
pm_caption += f"**╭────────────**\n"
pm_caption += f"┣»»»『{royal_mention}』«««\n"
pm_caption += f"┣ROYAL USERBOT ~ {ROYALversion}\n"
pm_caption += f"┣ROYAL  ~ [Owner](https://t.me/Samim3316)\n"
pm_caption += f"┣Support ~ [G𝖗ουρ](https://t.me/BR_guild)\n"
pm_caption += f"┣Řepô    ~ [Rєρο](https://github.com/THE-ROYALSBOT/ROYAL-USERBOT)\n"
pm_caption += f"|Youtube ~ [ BEWAFA ROYALS](https://www.youtube.com/channel/UCJh9x131aTSxV3xX6XiT8nA)\n"
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
