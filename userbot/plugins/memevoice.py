from ROYALBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot import bot
from userbot.cmdhelp import CmdHelp
from userbot.helpers.funct import deEmojify


@bot.on(admin_cmd(pattern="mev(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="mev(?: |$)(.*)", allow_sudo=True))
async def nope(royal):
    ROYAL = royal.pattern_match.group(1)
    if not ROYAL:
        if royal.is_reply:
            (await royal.get_reply_message()).message
        else:
            await edit_or_reply(
                royal,
                "`Sir please give some query to search and download it for you..!`",
            )
            return

    troll = await bot.inline_query("TrollVoiceBot", f"{(deEmojify(ROYAL))}")

    await troll[0].click(
        royal.chat_id,
        reply_to=royal.reply_to_msg_id,
        silent=True if royal.is_reply else False,
        hide_via=True,
    )
    await royal.delete()


CmdHelp("memevoice").add_command(
    "mev", "<meme txt>", "Searches and uploads the meme in voice format (if any)."
).add()
