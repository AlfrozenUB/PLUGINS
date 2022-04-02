from asyncio import create_subprocess_exec as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from ROYALBOT import CmdHelp
import os
import asyncio


@Rizoeluserbot.on(admin_cmd(outgoing=True, pattern="neofetch"))
@Rizoeluserbot.on(sudo_cmd(outgoing=True, pattern="neofetch", allow_sudo=True))
async def neofetchdetails(neofetch):
    """Neofetch For AlfrozenUserbot"""
    if not neofetch.text[0].isalpha() and neofetch.text[0] not in ("/", "#", "@", "!"):
        try:
            fetch = await asyncrunapp(
                "neofetch", "--stdout", stdout=asyncPIPE, stderr=asyncPIPE
            )

            stdout, stderr = await fetch.communicate()
            result = str(stdout.decode().strip()) + str(stderr.decode().strip())

            await neofetch.edit("`" + result + "`")
        except FileNotFoundError:
            await neofetch.edit("`Neofetch Not Found.. Please Install The Latest Version Of AlfrozenUserbot Or Get Help From Support Group` @ErineSupport")


CMD_HELP.update(
    {
        "neofetch": "➢ `.neofetch`\nUse - Neofetch"
    }
)
