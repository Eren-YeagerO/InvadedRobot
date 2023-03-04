import config
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

mongo = MongoClient(config.DB_URL)
dbname = mongo.MissKatyDB
