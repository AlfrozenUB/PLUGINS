import asyncio
import datetime

from telethon import events
from telethon.tl import functions, types

from ROYALBOT.utils import admin_cmd
from userbot import ALIVE_NAME
from userbot.cmdhelp import CmdHelp

global USER_night  # pylint:disable=E0602
global night_time  # pylint:disable=E0602
global last_night_message  # pylint:disable=E0602
USER_night = {}
night_time = None
last_night_message = {}

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ROYAL"


@borg.on(events.NewMessage(outgoing=True))  # pylint:disable=E0602
async def set_not_night(event):
    global USER_night  # pylint:disable=E0602
    global night_time  # pylint:disable=E0602
    global last_night_message  # pylint:disable=E0602
    current_message = event.message.message
    if ".night" not in current_message and "yes" in USER_night:  # pylint:disable=E0602
        try:
            await borg.send_message(  # pylint:disable=E0602
                Config.LOGGER_ID,  # pylint:disable=E0602
                f"Mine Owner has Gone to Sleep (Pure Din Sota hi Rehta He {DEFAULTUSER} )",
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            await borg.send_message(  # pylint:disable=E0602
                event.chat_id,
                "Please set `PLUGIN_CHANNEL` "
                + "for the proper functioning of night functionality "
                + "report in [ROYALBOT](t.me/BR_guild)\n\n `{}`".format(str(e)),
                reply_to=event.message.id,
                silent=True,
            )
        USER_night = {}  # pylint:disable=E0602
        night_time = None  # pylint:disable=E0602


@borg.on(admin_cmd(pattern=r"night ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    global USER_night  # pylint:disable=E0602
    global night_time  # pylint:disable=E0602
    global last_night_message  # pylint:disable=E0602
    global reason
    USER_night = {}
    night_time = None
    last_night_message = {}
    reason = event.pattern_match.group(1)
    if not USER_night:  # pylint:disable=E0602
        last_seen_status = await borg(  # pylint:disable=E0602
            functions.account.GetPrivacyRequest(types.InputPrivacyKeyStatusTimestamp())
        )
        if isinstance(last_seen_status.rules, types.PrivacyValueAllowAll):
            night_time = datetime.datetime.now()  # pylint:disable=E0602
        USER_night = f"yes: {reason}"  # pylint:disable=E0602
        if reason:
            await event.edit(f"мy мαѕτєя ιѕ gοιиg To sleep  Dnd нιм 🛏💤😴 ")
        else:
            await event.edit(f"My мαѕτєя is Going To Sleep")
        await asyncio.sleep(5)
        await event.delete()
        try:
            await borg.send_message(  # pylint:disable=E0602
                Config.PLUGIN_CHANNEL, f"My BOss Wants So Sleep"  # pylint:disable=E0602
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            logger.warn(str(e))  # pylint:disable=E0602


@borg.on(
    events.NewMessage(  # pylint:disable=E0602
        incoming=True, func=lambda e: bool(e.mentioned or e.is_private)
    )
)
async def on_night(event):
    if event.fwd_from:
        return
    global USER_night  # pylint:disable=E0602
    global night_time  # pylint:disable=E0602
    global last_night_message  # pylint:disable=E0602
    night_since = "**a while ago**"
    current_message_text = event.message.message.lower()
    if "night" in current_message_text:
        # userbot's should not reply to other userbot's
        # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
        return False
    if USER_night and not (await event.get_sender()).bot:  # pylint:disable=E0602
        if night_time:  # pylint:disable=E0602
            now = datetime.datetime.now()
            datime_since_night = now - night_time  # pylint:disable=E0602
            time = float(datime_since_night.seconds)
            days = time // (24 * 3600)
            time = time % (24 * 3600)
            hours = time // 3600
            time %= 3600
            minutes = time // 60
            time %= 60
            seconds = time
            if days == 1:
                night_since = "**Yesterday**"
            elif days > 1:
                if days > 6:
                    date = now + datetime.timedelta(
                        days=-days, hours=-hours, minutes=-minutes
                    )
                    night_since = date.strftime("%A, %Y %B %m, %H:%I")
                else:
                    wday = now + datetime.timedelta(days=-days)
                    night_since = wday.strftime("%A")
            elif hours > 1:
                night_since = f"`{int(hours)}h{int(minutes)}m` **ago**"
            elif minutes > 0:
                night_since = f"`{int(minutes)}m{int(seconds)}s` **ago**"
            else:
                night_since = f"`{int(seconds)}s` **ago**"
        msg = None
        message_to_reply = (
            f"мγ мαѕτєя нαѕ gοиє ƒοя ѕℓєєριиg\nѕιиϲє ωнєи:- {night_since}\nWhere He Is: **On Bed Sleeping** "
            + f"\n\n__ I'll back in a few Light years__\n**"
            if reason
            else f"**ιмροяταиτ иοτιϲє **\n\n{DEFAULTUSER} нαѕ ϐєєи gοиє ƒοя ѕℓєєριиg.\nѕιиϲє ωнєи:-{night_since}\n And Also Good [night To You...](https://telegra.ph/file/949056fe28ce6ed0d0b62.jpg) "
        )
        msg = await event.reply(message_to_reply)
        await asyncio.sleep(5)
        if event.chat_id in last_night_message:  # pylint:disable=E0602
            await last_night_message[event.chat_id].delete()  # pylint:disable=E0602
        last_night_message[event.chat_id] = msg  # pylint:disable=E0602


CmdHelp("night").add_command(
    "night",
    None,
    "Same like AFK. But fixed reason and for sleeping purpose only. Sed ;_;example:- .night <reason>",
).add()
