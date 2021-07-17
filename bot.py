import simplematrixbotlib as botlib
import os
import modules

import dotenv; dotenv.load_dotenv()

local_storage_path = os.getenv("STORAGE")
if not os.path.isdir(local_storage_path):
    os.mkdir(local_storage_path)

creds = botlib.Creds(
    os.getenv("HOMESERVER"),
    os.getenv("USERNAME"),
    os.getenv("PASSWORD"),
    f"{local_storage_path}/session.txt"
)

bot = botlib.Bot(creds)

bot.prefix = os.getenv("PREFIX")

admin_ids = []

bot_modules = [
    modules.BlockString(admin_ids, bot, f"{local_storage_path}/string_blocklist.txt")
]


bot.run()