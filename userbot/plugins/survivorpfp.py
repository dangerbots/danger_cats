"""
Time In Profile Pic.....
Command: `.appu`,.appudp,.epp

Custom / Modified Plugin for some magical effects by this Legendary Guy @Sur_vivor


#curse: who ever edits this credit section will goto hell

⚠️DISCLAIMER⚠️

USING THIS PLUGIN CAN RESULT IN ACCOUNT BAN + CAS BAN + SPAM BAN + ACCOUNT SUSPENSION . WE DONT CARE ABOUT BAN, SO WE ARR USING THIS.
"""
import asyncio
import os
import random
import shutil
from datetime import datetime

from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.errors import FloodWaitError
from telethon.tl import functions

from userbot.utils import admin_cmd

FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_FILE_TO_USEE = "userbot/helpers/styles/digital.ttf"

# Add telegraph media links of profile pics that are to be used
TELEGRAPH_MEDIA_LINKS = [
    "https://telegra.ph/file/fcda9959307eb4ef78c37.jpg",
    "https://telegra.ph/file/094eff3306c9e30479ca8.jpg",
    "https://telegra.ph/file/b450cb516181680d22bb5.jpg",
    "https://telegra.ph/file/1cd9690b3b6e2ea1611ec.jpg",
    "https://telegra.ph/file/bd8708a914046027240bd.jpg",
    "https://telegra.ph/file/4e5f907368c8d168885be.jpg",
    "https://telegra.ph/file/dffe4a944a3bf596fa41f.jpg",
    "https://telegra.ph/file/3d2d1f52d3df87ca19002.jpg",
    "https://telegra.ph/file/8d5b92925517c206fe6be.jpg",
    "https://telegra.ph/file/416a4bc6b3db00041f22d.jpg",
    "https://telegra.ph/file/fe6cc38245a171f712f1e.jpg",
    "https://telegra.ph/file/cdf95fae0e39edd0b2f5a.jpg",
    "https://telegra.ph/file/61d2d155d5199fc5c4b82.jpg",
    "https://telegra.ph/file/2851189ea7d8d3e686da0.jpg",
]

TELEGRAPH_MEDIA_LINKSS = [
    "https://telegra.ph/file/fcda9959307eb4ef78c37.jpg",
]

TELEGRAPH_MEDIA_LINKSSS = [
    "https://telegra.ph/file/b20273be27aeea4e8fcac.jpg",
]


@bot.on(admin_cmd(pattern="appu ?(.*)"))
async def autopic(event):
    while True:
        piclink = random.randint(0, len(TELEGRAPH_MEDIA_LINKS) - 1)
        AUTOPP = TELEGRAPH_MEDIA_LINKS[piclink]
        downloaded_file_name = "./userbot/original_pic.png"
        downloader = SmartDL(AUTOPP, downloaded_file_name, progress_bar=True)
        downloader.start(blocking=False)
        photo = "photo_pfp.png"
        while not downloader.isFinished():
            pass

        shutil.copy(downloaded_file_name, photo)
        Image.open(photo)
        current_time = datetime.now().strftime(
            "@Sur_vivor \n \nTime: %H:%M:%S \nDate: %d/%m/%y"
        )
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 23)
        drawn_text.text((350, 400), current_time, font=fnt, fill=(230, 230, 250))
        img.save(photo)
        file = await event.client.upload_file(photo)  # pylint:disable=E0602
        try:
            await event.client(
                functions.photos.UploadProfilePhotoRequest(file)  # pylint:disable=E0602
            )
            os.remove(photo)

            await asyncio.sleep(30)
        except:
            return


@bot.on(admin_cmd(pattern="appudp?(.*)"))
async def autopic(event):
    while True:
        piclink = random.randint(0, len(TELEGRAPH_MEDIA_LINKSS) - 1)
        AUTOPP = TELEGRAPH_MEDIA_LINKSS[piclink]
        downloaded_file_name = "./userbot/original_pic.png"
        downloader = SmartDL(AUTOPP, downloaded_file_name, progress_bar=True)
        downloader.start(blocking=False)
        photo = "photo_pfp.png"
        while not downloader.isFinished():
            pass
        shutil.copy(downloaded_file_name, photo)
        Image.open(photo)
        current_time = datetime.now().strftime("@CuTE_TeeN_rED\n\n  %H:%M:%S \n %d/%m/%y")
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USEE, 35)
        drawn_text.text((10, 40), current_time, font=fnt, fill=(255, 0, 0))
        img.save(photo)
        file = await event.client.upload_file(photo)  # pylint:disable=E0602
        try:
            await event.client(
                functions.photos.UploadProfilePhotoRequest(file)  # pylint:disable=E0602
            )
            os.remove(photo)

            await asyncio.sleep(90)
        except:
            return


@bot.on(admin_cmd(pattern="epp ?(.*)"))
async def autopic(event):
    while True:
        piclink = random.randint(0, len(TELEGRAPH_MEDIA_LINKSSS) - 1)
        AUTOPP = TELEGRAPH_MEDIA_LINKSSS[piclink]
        downloaded_file_name = "./userbot/original_pic.png"
        downloader = SmartDL(AUTOPP, downloaded_file_name, progress_bar=True)
        downloader.start(blocking=False)
        photo = "photo_pfp.png"
        while not downloader.isFinished():
            pass

        shutil.copy(downloaded_file_name, photo)
        Image.open(photo)
        current_time = datetime.now().strftime(
            "danger_of_telegram\n \nTime: %H:%M:%S \nDate: %d/%m/%y"
        )
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 23)
        drawn_text.text((50, 600), current_time, font=fnt, fill=(230, 230, 250))
        img.save(photo)
        file = await event.client.upload_file(photo)  # pylint:disable=E0602
        try:
            await event.client(
                functions.photos.UploadProfilePhotoRequest(file)  # pylint:disable=E0602
            )
            os.remove(photo)

            await asyncio.sleep(90)
        except:
            return


@bot.on(admin_cmd(pattern="cname"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    while True:
        DMY = time.strftime("%d.%m.%y")
        HM = time.strftime("%H:%M")
        name = f"{HM}🔥Տմɾѵíѵօɾ🔥{DMY}"
        logger.info(name)
        try:
            await borg(
                functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                    last_name=name
                )
            )
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)
        # else:
        # logger.info(r.stringify())
        # await borg.send_message(  # pylint:disable=E0602
        #     Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602
        #     "Changed Profile Picture"
        # )
        await asyncio.sleep(60)
