import asyncio

from userbot.plugins.sql_helper.mute_sql import is_muted, mute, unmute
from userbot.utils import admin_cmd


# @command(outgoing=True, pattern=r"^.gmute ?(\d+)?")
@borg.on(admin_cmd(pattern=r"fmute ?(\d+)?"))
async def startgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("Putting Dick🍆 💦 In Son mouth!!")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit(
            "Please reply to a user or add their into the command to fmute them."
        )
    event.chat_id
    await event.get_chat()
    if is_muted(userid, "fmute"):
        return await event.edit("This user is already fmuted")
    try:
        mute(userid, "fmute")
    except Exception as e:
        await event.edit("Error occured!\nError is " + str(e))
    else:
        await event.edit("Son Can't speek now.... Filled His Mouth With Cum😉")


# @command(outgoing=True, pattern=r"^.ungmute ?(\d+)?")
@borg.on(admin_cmd(pattern=r"unfmute ?(\d+)?"))
async def endgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit(
            "Taking Out Dick from Son mouth....\n\n       Today Sex Done😁 "
        )
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit(
            "Please reply to a user or add their into the command to ungmute them."
        )
    event.chat_id
    if not is_muted(userid, "fmute"):
        return await event.edit("This user is not gmuted")
    try:
        unmute(userid, "fmute")
    except Exception as e:
        await event.edit("Error occured!\nError is " + str(e))
    else:
        await event.edit("Son Feeling Good..... Now speak🍆🍆")


@command(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, "fmute"):
        await event.delete()
