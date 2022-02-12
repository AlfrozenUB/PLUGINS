import asyncio

from ROYALBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp
from userbot.plugins.sql_helper.mute_sql import is_muted, mute, unmute


@bot.on(admin_cmd(pattern="mute ?(\d+)?", outgoing=True))
@bot.on(sudo_cmd(pattern="mute ?(\d+)?", allow_sudo=True))
async def startmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await edit_or_reply(event, "Shut The Fukk Up!!!!!")
        await asyncio.sleep(3)
        private = True
    if any(
        [
            x in event.raw_text
            for x in (
                "/mute",
                "!mute",
                "amute",
                "bmute",
                "cmute",
                "dmute",
                "emute",
                "fmute",
                "gmute",
                "hmute",
                "imute",
                "jmute",
                "kmute",
                "lmute",
                "mmute",
                "nmute",
                "omute",
                "pmute",
                "qmute",
                "rmute",
                "smute",
                "tmute",
                "umute",
                "vmute",
                "wmute",
                "xmute",
                "ymute",
                "zmute",
            )
        ]
    ):
        await asyncio.sleep(0.5)
    else:
        reply = await event.get_reply_message()
        if event.pattern_match.group(1) is not None:
            userid = event.pattern_match.group(1)
        elif reply is not None:
            userid = reply.sender_id
        elif private is True:
            userid = event.chat_id
        else:
            return await edit_or_reply(
                event,
                "Please reply to a user or add their userid into the command to mute them.",
            )
        chat_id = event.chat_id
        chat = await event.get_chat()
        if "admin_rights" in vars(chat) and vars(chat)["admin_rights"] is not None:
            if chat.admin_rights.delete_messages is True:
                pass
            else:
                return await edit_or_reply(
                    event,
                    "`You can't mute a person if you dont have delete messages permission. ಥ﹏ಥ`",
                )
        elif "creator" in vars(chat):
            pass
        elif private == True:
            pass
        else:
            return await edit_or_reply(
                event, "I'm not admin here!! So i cant mute...😒🚶"
            )
        if is_muted(userid, chat_id):
            return await edit_or_reply(
                event, "This user is already muted in this chat ~~lmfao sed rip~~"
            )
        try:
            mute(userid, chat_id)
        except Exception as e:
            await edit_or_reply(event, "Error occured!\nError is " + str(e))
        else:
            await edit_or_reply(event, "Chup Hi Raho \n**｀-´)⊃━☆ﾟ.*･｡ﾟ **")


@bot.on(admin_cmd(pattern="unmute ?(\d+)?", outgoing=True))
@bot.on(sudo_cmd(pattern="unmute ?(\d+)?", allow_sudo=True))
async def endmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await edit_or_reply(event, "Unmutting!!!")
        await asyncio.sleep(3)
        private = True
    if any(
        [
            x in event.raw_text
            for x in (
                "/unmute",
                "!unmute",
                "aunmute",
                "bunmute",
                "cunmute",
                "dunmute",
                "eunmute",
                "funmute",
                "gunmute",
                "hunmute",
                "iunmute",
                "junmute",
                "kunmute",
                "lunmute",
                "munmute",
                "nunmute",
                "ounmute",
                "punmute",
                "qunmute",
                "runmute",
                "sunmute",
                "tunmute",
                "uunmute",
                "vunmute",
                "wunmute",
                "xunmute",
                "yunmute",
                "zunmute",
            )
        ]
    ):
        await asyncio.sleep(0.5)
    else:
        reply = await event.get_reply_message()
        if event.pattern_match.group(1) is not None:
            userid = event.pattern_match.group(1)
        elif reply is not None:
            userid = reply.sender_id
        elif private is True:
            userid = event.chat_id
        else:
            return await edit_or_reply(
                event,
                "Please reply to a user or add their userid into the command to unmute them.",
            )
        chat_id = event.chat_id
        if not is_muted(userid, chat_id):
            return await edit_or_reply(
                event, "__This user is not muted in this chat__\n（ ^_^）o自自o（^_^ ）"
            )
        try:
            unmute(userid, chat_id)
        except Exception as e:
            await edit_or_reply(event, "Error occured!\nError is " + str(e))
        else:
            await edit_or_reply(
                event, "Haa Abb Boll Bhai unmute successfully \n乁( ◔ ౪◔)「    ┑(￣Д ￣)┍"
            )


@command(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, event.chat_id):
        await event.delete()


CmdHelp("mute").add_command(
    "mute",
    "<reply to user>",
    "Its help U to mute Any user to group if u are admin then",
).add_command(
    "unmute", "<reply to user>", "Its help u to unmute any user if u are admin in group"
).add()
