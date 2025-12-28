import pymongo, os
from config import DB_URL,DB_NAME

dbclient = pymongo.MongoClient(mongodb+srv://aaravp4ajapat_db_user:5ikmuTNBwJu7nvn8@cluster0.ihvldiq.mongodb.net/)
database = dbclient[aaravp4ajapat_db_user]
user_data = database['users']



async def present_user(user_id : int):
    found = user_data.find_one({'_id': user_id})
    return bool(found)

async def add_user(user_id: int):
    user_data.insert_one({'_id': user_id})
    return

async def full_userbase():
    user_docs = user_data.find()
    user_ids = []
    for doc in user_docs:
        user_ids.append(doc['_id'])
        
    return user_ids

async def del_user(user_id: int):
    user_data.delete_one({'_id': user_id})
    return









# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
