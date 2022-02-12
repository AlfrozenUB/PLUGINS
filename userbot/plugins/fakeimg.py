import os

import requests

from ROYALBOT.utils import admin_cmd, sudo_cmd
from userbot import CmdHelp


@bot.on(admin_cmd(pattern="picgen"))
@bot.on(sudo_cmd(pattern="picgen", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return

    url = "https://thispersondoesnotexist.com/image"
    response = requests.get(url)
    await event.edit("`Creating a fake face...`")
    if response.status_code == 200:
        with open("ROYALBOT.jpg", "wb") as f:
            f.write(response.content)

    captin = f"Fake Image By ROYALBOT."
    fole = "ROYALBOT.jpg"
    await borg.send_file(event.chat_id, fole, caption=captin)
    await event.delete()
    os.system("rm /root/userbot/ROYALBOT.jpg ")


CmdHelp("fakeimg").add_command("picgen", None, "Fake Pic Generation").add()
