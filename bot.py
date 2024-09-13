# (c) github - @IllegalDeveloper ,telegram - https://telegram.me/illegal_Developer
# removing credits doesn't make you coder 


from pyrogram import Client
from pyrogram.enums import ParseMode
from datetime import datetime
from configs import Config
from aiohttp import web
import os
from helper import temp
from web import web_app
import asyncio

import logging
from logging.handlers import RotatingFileHandler
# Set the log file name
LOG_FILE_NAME = "Rkbotz_log_file.log"

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)

logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
    

PORT = int(os.environ.get('PORT', 8080))

class Bot(Client):
    def __init__(self):
        super().__init__(
            name=Config.BOT_USERNAME,
            api_hash=Config.API_HASH,
            api_id=Config.API_ID,
            plugins={"root": "plugins"},
            bot_token=Config.BOT_TOKEN
        )
        self.LOGGER = LOGGER  # Make sure LOGGER is defined elsewhere

    async def start(self):
        await super().start()
        temp.BOT = self
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()   
        
        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info("Bot Running..!\n\nCreated by \nhttps://t.me/Rk_botz")
        self.LOGGER(__name__).info(""" \n\n
        # (©)Rk_botz
        """)

        self.username = usr_bot_me.username
        

        # web-response
        app = web.AppRunner(web_app)
        await app.setup()
        await web.TCPSite(app, '0.0.0.0', PORT).start()


    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")

