from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot.cmdhelp import CmdHelp

from . import *


@bot.on(admin_cmd(pattern="findsong$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await edit_delete(event, "Reply to an audio message.")
        return
    reply_message = await event.get_reply_message()
    chat = "@auddbot"
    snku = await edit_or_reply(event, "Identifying the song")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(reply_message)
            check = await conv.get_response()
            if not check.text.startswith("Audio received"):
                return await snku.edit(
                    "An error while identifying the song. Try to use a 5-10s long audio message."
                )
            await snku.edit("Wait just a sec...")
            result = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await snku.edit("Please unblock (@auddbot) and try again")
            return
    namem = f"**Song Name : **{result.text.splitlines()[0]}\
        \n\n**Details : **__{result.text.splitlines()[2]}__"
    await snku.edit(namem)


CmdHelp("findsong").add_command(
    "findsong", None, "1st send song voice then reply to it and send .findsong"
).add()
