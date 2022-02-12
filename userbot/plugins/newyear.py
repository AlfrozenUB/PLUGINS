import asyncio

from ROYALBOT.utils import admin_cmd
from userbot.cmdhelp import CmdHelp

from . import *

file1 = "https://telegra.ph/file/fed9ae859812a1173f39d.mp4"
file2 = "https://telegra.ph/file/bd0d9edbd748d8a9a7d02.jpg"
file3 = "https://telegra.ph/file/2126757ff2390b7258559.jpg"
file4 = "https://telegra.ph/file/72e34dc425cddcdb5855f.jpg"
file5 = "https://telegra.ph/file/7ae5961e4022c0b0c3500.jpg"
file6 = "https://telegra.ph/file/e6b71c2f7cd63c7b0dadf.jpg"
file7 = "https://telegra.ph/file/ccfca771e268034fbfe6a.mp4"

edit_time = 10
hello_caption = "__The new year stands before us, like a chapter in a book, waiting to be written. We can help write that story by setting goals.__"


@bot.on(admin_cmd(pattern="hppynwyr(.*)"))
async def xd(event):
    await event.edit(
        "╭╮╱╭╮\n┃┃╱┃┃\n┃╰━╯┃\n┃╭━╮┃\n┃┃╱┃┃\n╰╯╱╰╯\n╭━━━╮\n┃╭━╮┃\n┃┃╱┃┃\n┃╰━╯┃\n┃╭━╮┃\n╰╯╱╰╯\n╭━━━╮\n┃╭━╮┃\n┃╰━╯┃\n┃╭━━╯\n┃┃\n╰╯\n╭━━━╮\n┃╭━╮┃\n┃╰━╯┃\n┃╭━━╯\n┃┃\n╰╯\n╭╮╱╱╭╮\n┃╰╮╭╯┃\n╰╮╰╯╭╯\n╱╰╮╭╯\n╱╱┃┃\n╱╱╰╯\n╭━╮╱╭╮\n┃┃╰╮┃┃\n┃╭╮╰╯┃\n┃┃╰╮┃┃\n┃┃╱┃┃┃\n╰╯╱╰━╯\n╭━━━╮\n┃╭━━╯\n┃╰━━╮\n┃╭━━╯\n┃╰━━╮\n╰━━━╯\n╭╮╭╮╭╮\n┃┃┃┃┃┃\n┃┃┃┃┃┃\n┃╰╯╰╯┃\n╰╮╭╮╭╯\n╱╰╯╰╯\n╭╮╱╱╭╮\n┃╰╮╭╯┃\n╰╮╰╯╭╯\n╱╰╮╭╯\n╱╱┃┃\n╱╱╰╯\n╭━━━╮\n┃╭━━╯\n┃╰━━╮\n┃╭━━╯\n┃╰━━╮\n╰━━━╯\n╭━━━ \n┃╭━╮┃\n┃┃╱┃┃\n┃╰━╯┃\n┃╭━╮┃\n╰╯╱╰╯\n╭━━━╮\n┃╭━╮┃\n┃╰━╯┃\n┃╭╮╭╯\n┃┃┃╰╮\n╰╯╰━╯"
    )
    event.pattern_match.group(1)
    async for tele in borg.iter_dialogs():
        lol = 0
        done = 0
        if tele.is_group:
            chat = tele.id
            try:
                on = await bot.send_file(chat, file=file1, caption=hello_caption)
                await asyncio.sleep(edit_time)
                ok = await bot.edit_message(chat, on, file=file2)
                await asyncio.sleep(edit_time)
                ok2 = await bot.edit_message(chat, ok1, file=file3)
                await asyncio.sleep(edit_time)
                ok3 = await bot.edit_message(chat, ok2, file=file4)
                await asyncio.sleep(edit_time)
                ok4 = await bot.edit_message(chat, ok3, file=file5)
                await asyncio.sleep(edit_time)
                ok5 = await bot.edit_message(chat, ok4, file=file6)
                await asyncio.sleep(edit_time)
                ok6 = await bot.edit_message(chat, ok5, file=file7)
                done += 1
            except:
                lol += 1
    await event.reply(
        f"🤗 ᵃᵈᵛᵃⁿᶜᵉ💞\n   ✨️ ʰᵃᵖᵖʸ ⁿᵉʷ ʸᵉᵃʳ✨️\n          💫 ᵐᵃʸ ᵗʰᵉ💫\n           🦋ⁿᵉʷ ʸᵉᵃʳ🦋\n          😘 ᵇˡᵉˢˢ ʸᵒᵘ😘\n  🤍🕊️ ʷⁱᵗʰ ʰᵉᵃˡᵗʰ🕊️🤍\n           🥳 ᵖʳᵒˢᵖᵉʳⁱᵗʸ🥳\n🥰🥰ᵃⁿᵈ ʰᵃᵖᵖⁱⁿᵉˢˢ🥰🥰\n"
    )


CmdHelp("happynewyear").add_command(
    "hppynwyr", None, "Wishs Happy New Year in all groups just one command"
).add_info("HAPPY NEW YEAR Wish Command").add_warning("Harmless Module✅").add_type(
    "Addons"
).add()
