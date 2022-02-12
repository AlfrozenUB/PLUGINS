import telethon
from telethon import Button, events, functions
from telethon.tl import functions, types
from telethon.tl.functions.channels import EditBannedRequest, GetFullChannelRequest
from telethon.tl.types import ChatBannedRights

import userbot.plugins.sql_helper.fsub_sql as sql
from userbot import bot
from userbot.utils import admin_cmd

royalbooy = bot.me.id
MUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=True)


async def is_admin(event, user):
    try:
        sed = await event.client.get_permissions(event.chat_id, user)
        if sed.is_admin:
            is_mod = True
        else:
            is_mod = False
    except:
        is_mod = False
    return is_mod


UNMUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=False)


async def check_him(channel, uid):
    try:
        result = await bot(
            functions.channels.GetParticipantRequest(channel=channel, user_id=uid)
        )
        return True
    except telethon.errors.rpcerrorlist.UserNotParticipantError:
        return False


async def rights(event):
    result = await bot(
        functions.channels.GetParticipantRequest(
            channel=event.chat_id,
            user_id=royalbooy,
        )
    )
    p = result.participant
    return isinstance(p, types.ChannelParticipantCreator) or (
        isinstance(p, types.ChannelParticipantAdmin) and p.admin_rights.ban_users
    )


@bot.on(admin_cmd(pattern="(fsub|forcesubscribe) ?(.*)"))
async def fs(event):
    permissions = await bot.get_permissions(event.chat_id, event.sender_id)
    if not permissions.is_admin:
        return await event.reply(
            "❗**Group admin Required**\nYou have to be the group creator or admin to do that."
        )
    if not await is_admin(event, royalbooy):
        return await event.reply("I'm not an admin Mind Promoting Me?!")
    args = event.pattern_match.group(2)
    channel = args.replace("@", "")
    if args == "on" or args == "On":
        return await event.reply("❗Please Specify the Channel Username")
    if args in ("off", "no", "disable"):
        sql.disapprove(event.chat_id)
        await event.reply("❌ **Force Subscribe is Disabled Successfully.**")
    else:
        try:
            ch_full = await bot(GetFullChannelRequest(channel=channel))
        except Exception as e:
            await event.reply(f"{e}")
            return await event.reply("❗**Invalid Channel Username.**")
        rip = await check_him(channel, royalbooy)
        if rip is False:
            return await event.reply(
                f"❗**Not an Admin in the Channel**\nI am not an admin in the [channel](https://t.me/{args}). Add me as a admin in order to enable ForceSubscribe.",
                link_preview=False,
            )
        sql.add_channel(event.chat_id, str(channel))
        await event.reply(f"✅ **Force Subscribe is Enabled** to @{channel}.")


@bot.on(events.NewMessage(pattern=None))
async def f(event):
    chat_id = event.chat_id
    chat_db = sql.fs_settings(chat_id)
    event.sender_id
    if not chat_db:
        return
    if await is_admin(event, event.sender_id):
        return
    if chat_db:
        try:
            channel = chat_db.channel
            chat_id = event.chat_id
            chat_db = sql.fs_settings(chat_id)
            channel = chat_db.channel
            grp = f"t.me/{channel}"
            rip = await check_him(channel, event.sender_id)
            if rip is False:
                await bot.send_message(
                    event.chat_id, f"join [group]({grp})", link_preview=False
                )
                royalboy = Config.BOT_USERNAME
                await bot(
                    EditBannedRequest(event.chat_id, event.sender_id, MUTE_RIGHTS)
                )
                response = await bot.inline_query(royalboy, "pm_warn")
                await response[0].click(event.chat_id)
                await event.delete()
        except:
            if not await rights(event):
                await bot.send_message(
                    event.chat_id,
                    "❗**I am not an admin here.**\nMake me admin with ban user permission",
                )


try:
    global rk
    rk = rk
except:
    rk = "chutia"


@bot.on(events.InlineQuery(pattern="royalbooy"))
async def NOOBBOY(event):
    global rk
    event.builder
    royalproboy = [[Button.inline("Unmute Me 😊", data="LeGeNd")]]
    NOOBBOYOP = royalboy.article(
        title="FORCE SUBSCRIBE", text="fsub", buttons=royalproboy
    )
    await event.answer([NOOBBOYOP])


import re


@bot.on(events.callbackquery.CallbackQuery(re.compile(b"LeGeNd")))
async def start_again(event):
    try:
        tata = event.pattern_match.group(1)
        data = tata.decode()
        user = data.split("_", 1)[1]
    except:
        pass
    if not event.sender_id == int(user):
        return await event.answer("You are not the muted user!")
    chat_id = event.chat_id
    chat_db = sql.fs_settings(chat_id)
    if chat_db:
        channel = chat_db.channel
        rip = await check_him(channel, event.sender_id)
        if rip is True:
            try:
                await event.delete()
                await bot(EditBannedRequest(event.chat_id, int(user), UNMUTE_RIGHTS))
            except:
                if not await rights(event):
                    return await bot.send_message(
                        event.chat_id,
                        "❗ **I am not an admin here.**\nMake me admin with ban user permission",
                    )
        else:
            await event.answer("Please join the Channel!")
