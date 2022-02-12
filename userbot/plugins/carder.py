from faker import Faker
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from ROYALBOT import CmdHelp
from ROYALBOT import bot as ROYALBOT
from ROYALBOT.utils import admin_cmd, edit_or_reply, sudo_cmd


@ROYALBOT.on(admin_cmd("gencc$"))
@ROYALBOT.on(sudo_cmd("gencc$", allow_sudo=True))
async def _(ROYALevent):
    if ROYALevent.fwd_from:
        return
    ROYALcc = Faker()
    ROYALname = ROYALcc.name()
    ROYALadre = ROYALcc.address()
    ROYALcard = ROYALcc.credit_card_full()

    await edit_or_reply(
        ROYALevent,
        f"__**👤 NAME :- **__\n`{ROYALname}`\n\n__**🏡 ADDRESS :- **__\n`{ROYALadre}`\n\n__**💸 CARD :- **__\n`{ROYALcard}`",
    )


@ROYALBOT.on(admin_cmd(pattern="bin ?(.*)"))
@ROYALBOT.on(sudo_cmd(pattern="bin ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    ROYAL_input = event.pattern_match.group(1)
    chat = "@szbinscheckerbot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=2143004427)
            )
            await event.client.send_message(chat, f"/bin {ROYAL_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @szbinscheckerbot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@ROYALBOT.on(admin_cmd(pattern="register ?(.*)"))
@ROYALBOT.on(sudo_cmd(pattern="register ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    ROYAL_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1247032902)
            )
            await event.client.send_message(chat, f"/register {ROYAL_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@ROYALBOT.on(admin_cmd(pattern="password ?(.*)"))
@ROYALBOT.on(sudo_cmd(pattern="password ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    ROYAL_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1247032902)
            )
            await event.client.send_message(chat, f"/password {ROYAL_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


CmdHelp("carder").add_command("gencc", None, "Generates fake cc...").add_command(
    "register", None, "Register Ur Account Here"
).add_command("password", "<enter>", "Set ur Account Password On CXM.CARDS").add()
