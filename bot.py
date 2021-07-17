import simplematrixbotlib as botlib
import os

import dotenv; dotenv.load_dotenv()

local_storage_path = "./.storage/"

creds = botlib.Creds(
    os.getenv("HOMESERVER"),
    os.getenv("USERNAME"),
    os.getenv("PASSWORD"),
    f"{local_storage_path}/session.txt"
)