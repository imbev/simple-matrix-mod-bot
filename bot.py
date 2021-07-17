import simplematrixbotlib as botlib
import os

import dotenv; dotenv.load_dotenv()

local_storage_path = "./.storage/"
if not os.path.isdir(local_storage_path):
    os.mkdir(local_storage_path)

creds = botlib.Creds(
    os.getenv("HOMESERVER"),
    os.getenv("USERNAME"),
    os.getenv("PASSWORD"),
    f"{local_storage_path}/session.txt"
)

bot = botlib.Bot(creds)

bot.prefix = "/"

bot.run()