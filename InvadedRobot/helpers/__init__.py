import config
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

mongodb = MongoClient(config.DB_URL)
dbname = mongodb.MissKatyDB
