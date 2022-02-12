# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2

from ROYALBOT.utils import admin_cmd, sudo_cmd
from userbot.cmdhelp import CmdHelp


@bot.on(admin_cmd(pattern=r"tagall (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern=r"tagall (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    mentions = event.pattern_match.group(1)
    if mentions:
        chat = await event.get_input_chat()
        async for x in borg.iter_participants(chat, 200):
            mentions += f" \n\n [{x.first_name}](tg://user?id={x.id})"
        reply_message = None
        if event.reply_to_msg_id:
            reply_message = await event.get_reply_message()
            await reply_message.reply(mentions)
        else:
            await event.reply(mentions)
    else:
        chat = await event.get_input_chat()
        async for y in borg.iter_participants(chat, 100):
            hello = f"Hi, How Are U\n\n [{y.first_name}](tg://user?id={y.id})"
        reply_message = None
        if event.reply_to_msg_id:
            reply_message = await event.get_reply_message()
            await reply_message.reply(hello)
        else:
            await event.reply(hello)
    await event.delete()


"""@bot.on(admin_cmd(pattern=r"admins", outgoing=True))
@bot.on(sudo_cmd(pattern=r"admins", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    mentions = "Administrators : "
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()
"""

CmdHelp("tags").add_command(
    "tagall", "<text>", "Tags all the members in the group. (Max 100)"
).add_command("admin", None, "Tags all the admins in the group").add()
