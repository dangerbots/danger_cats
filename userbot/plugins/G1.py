from telethon import events
import asyncio
import os
import sys
from userbot import utils


@borg.on(utils.admin_cmd(pattern="g1 ?(.*)"))
async def payf(event):
    paytext=event.pattern_match.group(1)
    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1,paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1,paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1,paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1,paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1,paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1,paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1,paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1,paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1,paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1, paytext*1)
    await event.edit(pay)
