from telethon import events

from userbot import *

from . import *

PM_IMG = "https://telegra.ph/file/b4c7082f2c22283d66394.jpg"
pm_caption = f"⚜『Alfrozen Usebrbot』Is Ôñĺîne⚜ \n\n"
pm_caption += f"Ôwñêř ~ 『{royal_mention}』\n"
pm_caption += f"**╭───────────**\n"
pm_caption += f"┣Ťêlethon ~ `1.15.0` \n"
pm_caption += f"┣『Alfrozen Usebrbot』~ `{ROYALversion}` \n"
pm_caption += f"┣Çhâññel ~ [Channel](https://t.me/Alfrozen)\n"
pm_caption += f"┣**License** ~ [License v3.0](github.com/Kajukatliii/AlfrozenUB/blob/master/LICENSE)\n"
pm_caption += f"┣Copyright ~ By [『Alfrozen Usebrbot』 ](https://t.me/animechataura)\n"
pm_caption += f"┣Owner ~ By [『Elliot』 ](https://t.me/Its_RoyalBoy)\n"
pm_caption += f"╰────────────\n"
pm_caption += f"       »»» [『Alfrozen Usebrbot』](https://t.me/AlfrozenUB) «««"


@tgbot.on(events.NewMessage(pattern="^/alive"))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
