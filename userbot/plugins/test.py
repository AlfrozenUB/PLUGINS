import asyncio

from ROYALBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp


@bot.on(admin_cmd(pattern="test ?(.*)"))
@bot.on(sudo_cmd(pattern="test ?(.*)", allow_sudo=True))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):

        await edit_or_reply(event, "`Testing ROYALBOT`")
        await asyncio.sleep(1)
        await edit_or_reply(event, "`Testing ROYALBOT.`")
        await asyncio.sleep(1)
        await edit_or_reply(event, "`Testing ROYALBOT..`")
        await asyncio.sleep(1)
        await edit_or_reply(event, "`Testing ROYALBOT...`")
        await asyncio.sleep(1)
        await edit_or_reply(event, "`Testing ROYALBOT....`")
        await asyncio.sleep(1)
        await edit_or_reply(event, "`Testing ROYALBOT.....`")
        await asyncio.sleep(2)
        await edit_or_reply(event, "__Testing Successful__")
        await asyncio.sleep(2)
        await edit_or_reply(event, "`Generating Output`\nPlease wait")
        await asyncio.sleep(2)
        await edit_or_reply(event, "__Output Generated Successfully__")
        await asyncio.sleep(2)
        await edit_or_reply(event, "**SAVING OUTPUT TO ROYALBOT LOCAL DATABASE**")
        await asyncio.sleep(3.5)
        await edit_or_reply(
            event,
            "Your [ROYALBOT](https:/t.me/BR_guild) is working Fine...\n       Join @BR_guild For Any Help......",
        )


CmdHelp("test").add_command(
    "test", None, "Test wether your bot is running or not."
).add()
