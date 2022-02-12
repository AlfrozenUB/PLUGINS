from telethon import events

from userbot import *

from . import *

PM_IMG = "https://telegra.ph/file/c26fc61e904476083baa7.jpg"
pm_caption = f"⚜『ROYAL USERBOT』Is Ôñĺîne⚜ \n\n"
pm_caption += f"Ôwñêř ~ 『{royal_mention}』\n"
pm_caption += f"**╭───────────**\n"
pm_caption += f"┣Ťêlethon ~ `1.15.0` \n"
pm_caption += f"┣『ROYAL USERBOT』~ `{ROYALversion}` \n"
pm_caption += f"┣Çhâññel ~ [Channel](https://t.me/Its_RoyalBot)\n"
pm_caption += f"┣**License** ~ [License v3.0](github.com/The-RoyalBot/LEGENBOT/blob/master/LICENSE)\n"
pm_caption += f"┣Copyright ~ By [『ROYAL USERBOT』 ](https://t.me/BR_guild)\n"
pm_caption += f"┣Assistant ~ By [『THE ROYALS』 ](https://t.me/Its_RoyalBoy)\n"
pm_caption += f"╰────────────\n"
pm_caption += f"       »»» [『ROYAL USERBOT』](https://t.me/BR_guild) «««"


@tgbot.on(events.NewMessage(pattern="^/alive"))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
