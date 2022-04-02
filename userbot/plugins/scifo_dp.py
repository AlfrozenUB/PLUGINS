import asyncio
import os
import random
import re
import urllib
import requests
from telethon.tl import functions
from ROYALBOT.utils import admin_cmd
from userbot import CMD_HELP

COLLECTION_STRING = [
    "star-wars-wallpaper-1080p",
    "4k-sci-fi-wallpaper",
    "star-wars-iphone-6-wallpaper",
    "kylo-ren-wallpaper",
    "darth-vader-wallpaper",
]


async def scifipp():

    rnd = random.randint(0, len(COLLECTION_STRING) - 1)
    pack = COLLECTION_STRING[rnd]
    plist = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile(r"/\w+/full.+.jpg")
    f = f.findall(plist)
    fy = "http://getwallpapers.com" + random.choice(f)
    print(fy)

    if not os.path.exists("f.ttf"):

        urllib.request.urlretrieve(
            "https://github.com/MrRizoel/Rizoeluserbot/raw/master/Extras/RiZoeL.ttf",
            "f.ttf",
        )

    r = requests.get(fy, allow_redirects=True)
    open('Rizoeluserbotautopic.jpg', 'wb').write(r.content)


@Rizoeluserbot.on(admin_cmd(pattern="scidp ?(.*)"))
async def main(event):

    await event.edit(
        "**Starting Automatic Sci-Fi Profile Pic**.\n`Please Note That It Will Automatically Update Your Profile Pic After 10 Minutes`\nBy Your [AlfrozenUserbot](https://github.com/AlfrozenUB/ALfrozenUB)"
    )

    while True:

        await scifipp()
        file = await event.client.upload_file("Rizoeluserbotautopic.jpg")
        await event.client(functions.photos.UploadProfilePhotoRequest(file))
        os.system("rm -rf Rizoeluserbotautopic.jpg")
        await asyncio.sleep(600)


CMD_HELP.update({"scifidp": ".scifidp\nUse - Autochanging Sci-Fi Profile Pic."})
