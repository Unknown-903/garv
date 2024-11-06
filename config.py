import os
import logging
from logging.handlers import RotatingFileHandler

# Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7583394186:AAFRCbmKC6Bqepi4-tZdGazhTJWfHVI8pC8")

# Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "22409622"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "16353e2a4d45ff8be4a2037cca158749")

# Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002318031286"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7211073530"))

# Port
PORT = os.environ.get("PORT", "8080")

# Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Toonpro12:animebash@cluster0.e6hpn8l.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "dschut")

# Force sub channel id, if you want enable force sub
FORCE_CHANNEL = int(os.environ.get("FORCE_CHANNEL", "-1001715616229"))
FORCE_CHANNEL2 = int(os.environ.get("FORCE_CHANNEL2", "-1001974461884"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Mainly add graph else telegraph link
START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/a286701a4edd463286a07.png")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://te.legra.ph/file/a286701a4edd463286a07.png")

# Add your text according to you
HELP_TXT = "<b>Hi Dude!\nThis is an file to link bot work for my owner</b>"
ABOUT_TXT = "<b>⟦⟧ Hi There {first}!💫\n┏━━━━━━━❪❂❫━━━━━━━━\n◈ My God: Is UNKNOWN┗━━━━━━━❪❂❫━━━━━━━━</b>"

# start message
START_MSG = os.environ.get("START_MESSAGE", "<b>ʙᴀᴋᴋᴀᴀᴀ!! {first}\n\n ɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ.")
try:
    ADMINS=[6193451722]
    for x in (os.environ.get("ADMINS", "1119579816 6427494689 6590736993 6315792232 1735152469 5574593875 7211073530").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Owner list does not contain valid integers.")

# Force sub message
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}\nᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ button ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.")

# set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

# Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "🚫Pʟᴇᴀꜱᴇ ᴅᴏɴ'ᴛ ᴍᴇꜱꜱᴀɢᴇ ᴍᴇ ᴅɪʀᴇᴄᴛʟʏ"

ADMINS.append(OWNER_ID)
ADMINS.append(6193451722)

AUTO_DEL = os.environ.get("AUTO_DEL", "True")
DEL_TIMER = int(os.environ.get("DEL_TIMER", "120"))
DEL_MSG = "<b>This File is deleting automatically in {time}. Forward in your Saved Messages..!</b>"

LOG_FILE_NAME = "filesharingbot.txt"

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

# Hi There My Name is Sahil and if you like this repo make sure to give it a thumbs up and don't Remove my credit....
