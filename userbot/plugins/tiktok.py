""" tiktok downloaded plugin creted by @mrconfused and @sandy1709 


Dont edit credits """
from telethon.errors.rpcerrorlist import YouBlockedUserError

from ROYALBOT.utils import admin_cmd
from userbot.cmdhelp import CmdHelp


@bot.on(admin_cmd("tti ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    d_link = event.pattern_match.group(1)
    if ".com" not in d_link:
        await event.edit("` I need a link to download something pro.`**(._.)**")
        return
    else:
        await event.edit("downloading your video")
    bot = "@HK_tiktok_BOT"

    async with bot.conversation("@HK_tiktok_BOT") as conv:
        try:
            await conv.send_message(d_link)
            await conv.get_response()
            details = await conv.get_response()
            if details.text.startswith("Sorry"):
                await bot.send_message(event.chat_id, "sorry . something went wrong")
                return
            await conv.get_response()
            await conv.get_response()
            await bot.send_file(event.chat_id, details, caption=details.text)
            await event.delete()
        except YouBlockedUserError:
            await event.edit("**Error:** `unblock` @HK_tiktok_BOT `and retry!`")


@bot.on(admin_cmd("ttv ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    d_link = event.pattern_match.group(1)
    if ".com" not in d_link:
        await event.edit("` I need a link to download something pro.`**(._.)**")
        return
    else:
        await event.edit("doownloading your video")
    bot = "@HK_tiktok_BOT"

    async with bot.conversation("@HK_tiktok_BOT") as conv:
        try:
            await conv.send_message(d_link)
            await conv.get_response()
            details = await conv.get_response()
            if details.text.startswith("Sorry"):
                await bot.send_message(event.chat_id, "sorry . something went wrong")
                return
            await conv.get_response()
            cat3 = await conv.get_response()
            await bot.send_file(event.chat_id, cat3)
            await event.delete()
        except YouBlockedUserError:
            await event.edit("**Error:** `unblock` @HK_tiktok_BOT `and retry!`")


@bot.on(admin_cmd("wttv ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    d_link = event.pattern_match.group(1)
    if ".com" not in d_link:
        await event.edit("` I need a link to download something pro.`**(._.)**")
        return
    else:
        await event.edit("doownloading your video")
    bot = "@HK_tiktok_BOT"

    async with bot.conversation("@HK_tiktok_BOT") as conv:
        try:
            await conv.send_message(d_link)
            await conv.get_response()
            details = await conv.get_response()
            if details.text.startswith("Sorry"):
                await bot.send_message(event.chat_id, "sorry . something went wrong")
                return
            cat2 = await conv.get_response()
            await conv.get_response()
            await bot.send_file(event.chat_id, cat2)
            await event.delete()
        except YouBlockedUserError:
            await event.edit("**Error:** `unblock` @HK_tiktok_BOT `and retry!`")


CmdHelp("tiktok").add_command(
    "tti", None, "Shows you the information of the given tiktok video link."
).add_command(
    "ttv", None, "Sends you the tiktok video of the given link without watermark"
).add_command(
    "wttv", None, "Sends you the tiktok video of the given link without watermark"
).add()
