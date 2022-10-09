import os
import config
import logging

from pyrogram import Client
from pymongo import MongoClient

# enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('logs.txt'),
              logging.StreamHandler()],
    level=logging.INFO)

LOGGER = logging.getLogger(__name__)


#pyrogram bot client start
plugins = dict(root="InvadedRobot")
bot = Client(name=str(config.USERNAME), 
             api_id=config.API_ID, 
             api_hash=config.API_HASH,
             bot_token=config.BOT_TOKEN,
             plugins=plugins)

# mongodb from pymongo #
pymongo = MongoClient(config.DB_URL)
pymongodb = pymongo.bot