from InvadedRobot.helpers import *

troopsdb = mongodb.troopdb

async def get_troops() -> list:
    troop_users = await troopsdb.find_one({"user_id": "user_id"})
    if not troop_users:
        return []
    return troop_users["troop_users"]

async def add_troop(user_id: int):
      troop_users = await get_troops()
      troop_users.append(user_id)
      await troopsdb.update_one(
        {"user_id": "user_id"}, {"$set": {"troop_users": troop_users}}, upsert=True)
      return True  

async def remove_troop(user_id: int):
       troop_users = await get_troops()
       troop_users.remove(user_id)
       await troopsdb.update_one(
        {"user_id": "user_id"}, {"$set": {"troop_users": troop_users}}, upsert=True)
       return True
