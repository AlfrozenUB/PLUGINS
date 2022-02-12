import io
import math
import random

from PIL import Image
from telethon.tl.types import (
    DocumentAttributeFilename,
    DocumentAttributeSticker,
    MessageMediaPhoto,
)

from userbot.utils import *

from . import *

ROYAL = [
    "Wait Few Minute...",
    "Wait A Sec Processing...",
]

royal = Config.CUSTOM_STICKER_PACK_NAME


@bot.on(admin_cmd(outgoing=True, pattern="png"))
@bot.on(sudo_cmd(pattern="png", allow_sudo=True))
async def kang(args):
    user = await bot.get_me()
    if not user.username:
        user.username = user.first_name
    message = await args.get_reply_message()
    photo = None
    emojibypass = False
    is_anim = False

    if message and message.media:
        if isinstance(message.media, MessageMediaPhoto):
            photo = io.BytesIO()
            photo = await bot.download_media(message.photo, photo)
        elif "image" in message.media.document.mime_type.split("/"):
            photo = io.BytesIO()
            await bot.download_file(message.media.document, photo)
            if (
                DocumentAttributeFilename(file_name="sticker.webp")
                in message.media.document.attributes
            ):
                message.media.document.attributes[1].alt
                emojibypass = True
        elif "tgsticker" in message.media.document.mime_type:
            await args.edit(f"`{random.choice(ROYAL)}`")
            await bot.download_file(message.media.document, "AnimatedSticker.tgs")

            attributes = message.media.document.attributes
            for attribute in attributes:
                if isinstance(attribute, DocumentAttributeSticker):
                    attribute.alt

            emojibypass = True
            is_anim = True
            photo = 1
        else:
            await args.edit("`Unsupported File!`")
            return
    else:
        await args.edit("`I can't kang that...`")
        return

    if photo:
        splat = args.text.split()
        if not emojibypass:
            pass
        pack = 1
        if len(splat) == 3:
            pack = splat[2]  # User sent both
            splat[1]
        elif len(splat) == 2:
            if splat[1].isnumeric():
                # User wants to push into different pack, but is okay with
                # thonk as emote.
                pack = int(splat[1])
            else:
                # User sent just custom emote, wants to push to default
                # pack
                splat[1]

        packname = f"{user.username}"
        packnick = (
            f"{royal} Vol.{pack}"
            if royal
            else f"@{user.username}'s royal Vol.{pack}"
        )
        file = io.BytesIO()
        await args.delete()

        if not is_anim:
            image = await resize_photo(photo)
            file.name = "sticker.png"
            image.save(file, "PNG")
        else:
            packname += "_anim"
            packnick += " (Animated)"
        if is_anim:
            await bot.send_file(arg.chat_id, "AnimatedSticker.tgs")
            remove(args.chat_id, "AnimatedSticker.tgs")
        else:
            file.seek(0)
            await bot.send_file(args.chat_id, file, force_document=True)
    #  await bot.send_file(args.chat_id, packnick, caption=f"Hello")


async def resize_photo(photo):
    """Resize the given photo to 512x512"""
    image = Image.open(photo)
    maxsize = (512, 512)
    if (image.width and image.height) < 512:
        size1 = image.width
        size2 = image.height
        if image.width > image.height:
            scale = 512 / size1
            size1new = 512
            size2new = size2 * scale
        else:
            scale = 512 / size2
            size1new = size1 * scale
            size2new = 512
        size1new = math.floor(size1new)
        size2new = math.floor(size2new)
        sizenew = (size1new, size2new)
        image = image.resize(sizenew)
    else:
        image.thumbnail(maxsize)

    return image


from userbot.cmdhelp import CmdHelp

CmdHelp("png").add_command(
    "png", "<reply to image/sticker>", "Its Help U To Convert Into Png File"
).add()
