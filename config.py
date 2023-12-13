from os import getenv
from dotenv import load_dotenv
load_dotenv()

API_ID = int(getenv("API_ID", None))
API_HASH = getenv("API_HASH", None)
BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_ID = int(getenv("OWNER_ID", None)
LOGGER_ID = int(getenv("LOGGER_ID", None)
MONGO_URI = getenv("MONGO_URI" , None)
DOWNLOAD_LOCATION = getenv("DOWNLOAD_LOCATION","./DOWNLOAD/")
