import os
import logging
from logging.handlers import RotatingFileHandler




BOT_TOKEN = os.environ.get("BOT_TOKEN", "8023415791:AAEp-YRhsXrQhBY-lptelwmtVKEXtW60BQg")
API_ID = int(os.environ.get("API_ID", "33555874"))
API_HASH = os.environ.get("API_HASH", "0925ddfb14a82c71de08b93e53c440f3")


OWNER_ID = int(os.environ.get("OWNER_ID", "@AP_Ichigo_Kurosaki"))
DB_URL = os.environ.get("DB_URL", "https://console.firebase.google.com/project/my-file-sharing-bot/database/my-file-sharing-bot-default-rtdb/data/~2F?fb_gclid=Cj0KCQiApL7KBhC7ARIsAD2Xq3Atk9FFhZwZ_vikOqWsA0qzp3K4SU90ZkUVo3XCknx_B9VoaFWprKEaAgKlEALw_wcB")
DB_NAME = os.environ.get("DB_NAME", "My File sharing bot")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "https://t.me/+PUUjPCL4L8YzZDU9"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))


FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "600")) # auto delete in seconds


PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))



try:
    ADMINS=[6848088376]
    for x in (os.environ.get("ADMINS", "6848088376").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")









CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", ⌜━━━━━━━━━━━━━━━━━━━⌝
•  𝗧𝗵𝗲 𝗔𝗰𝗲 𝗡𝗲𝘁𝘄𝗼𝗿𝗸 (https://t.me/The_Ace_Network)
│───────────────────────│
☞ Mᴀɪɴ Cʜᴀɴɴᴇʟ: ᴛʜᴇ ᴀᴄᴇ ᴇᴍᴘᴇʀᴏʀ (https://t.me/The_Ace_Emperor)
│───────────────────────│
☞ ᴇɴɢʟɪꜱʜ Aɴɪᴍᴇ: 𝗧ʜᴇ 𝗔ᴄᴇ 𝗖ᴏꜱᴍᴏꜱ (https://t.me/The_Anime_Cosmos) 
☞ ʜɪɴᴅɪ Aɴɪᴍᴇ: 𝗧ʜᴇ 𝗔ᴄᴇ 𝗔ɴɪᴍᴇ (https://t.me/The_Ace_Anime)
│───────────────────────│
☞ ʜɪɴᴅɪ Oɴɢᴏɪɴɢ: 𝗧ʜᴇ 𝗔ᴄᴇ 𝗢ɴɢᴏɪɴɢ (https://t.me/The_Ace_Ongoing)
☞ ᴇɴɢʟɪꜱʜ Oɴɢᴏɪɴɢ: 𝗧ʜᴇ 𝗢ɴɢᴏɪɴɢ 𝗖ᴏꜱᴍᴏꜱ (https://t.me/The_Ongoing_Cosmos)
│───────────────────────│
☞ Mᴀɴʜᴡᴀ Cʜᴀɴɴᴇʟ: 𝗧ʜᴇ 𝗠ᴀɴʜᴡᴀ 𝗘ᴍᴘᴇʀᴏʀ (https://t.me/The_Manhwa_Emperor)
☞ Mᴀɴɢᴀ Cʜᴀɴɴᴇʟ: 𝗧ʜᴇ 𝗠ᴀɴɢᴀ 𝗘ᴍᴘᴇʀᴏʀ (https://t.me/The_Manga_Emperor)
│───────────────────────│
❐ Nᴇᴛᴡᴏʀᴋ: ᴛʜᴇ ᴀᴄᴇ ɴᴇᴛᴡᴏʀᴋ (https://t.me/The_Ace_Network)
│───────────────────────│
❃ Mᴏᴠɪᴇs Cʜᴀɴɴᴇʟ: ғʟɪx ᴠᴇʀsᴇ (http://t.me/Flix_Verse)
❃ σтт Cʜᴀɴɴᴇʟ: 𝗧ʜᴇ 𝗢ᴍɴɪꜱᴇʀɪᴇꜱ (https://t.me/The_Omniseries) 
❃ Aᴅᴜʟᴛ Nᴇᴛᴡᴏʀᴋ: 𝗧ʜᴇ 𝗖ᴜʟᴛᴜʀᴇᴅ 𝗗ɪꜱᴛʀɪᴄᴛ (https://t.me/The_Cultured_District)
│───────────────────────│
 (https://t.me/+lB05vD5bGyszMzg1)❐ Rᴇǫ/Cʜᴀᴛ: 𝘾𝙝𝙖𝙩𝙞𝙣𝙜 𝙃𝙪𝙗 (https://t.me/+lB05vD5bGyszMzg1)
 ⌞━━━━━━━━━━━━━━━━━━━⌟)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', "True") == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"







USER_REPLY_TEXT = "❌Don't Send Me Messages Directly I'm Only File Share Bot !"

START_MSG = os.environ.get("START_MESSAGE", "Hello {mention}\n\nI Can Store Private Files In Specified Channel And Other Users Can Access It From Special Link.")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {mention}\n\n<b>You Need To Join In My Channel/Group To Use Me\n\nKindly Please Join Channel</b>")





ADMINS.append(OWNER_ID)
ADMINS.append(6848088376)

LOG_FILE_NAME = "filesharingbot.txt"

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
   





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
