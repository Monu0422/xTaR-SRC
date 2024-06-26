import time
import os
import logging
import json
from telethon import events
from pyrogram.errors import FloodWait
from .. import bot as gagan
from .. import userbot, Bot
from .. import FORCESUB as fs
from main.plugins.pyroplug import get_msg, ggn_new
from main.plugins.helpers import get_link, join, screenshot
from main.plugins.helpers import force_sub

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.INFO)
logging.getLogger("telethon").setLevel(logging.INFO)

ft = f"To use this bot you've to join @{fs}."
message = "Send me the message link you want to start saving from, as a reply to this message."

process = []
timer = []
user = []

# List of commands that should bypass the link check
commands = ['/dl']  # Add other commands as needed

@gagan.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def clone(event):
    logging.info(event)
    file_name = ''

    # Check if the message starts with a command
    if any(event.message.text.startswith(command) for command in commands):
        # Command detected, bypass link check and do nothing
        return

    if event.is_reply:
        reply = await event.get_reply_message()
        if reply.text == message:
            return

    
        ind = user.index(f'{int(event.sender_id)}')
        user.pop(int(ind))
        time.sleep(1)

