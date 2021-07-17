import simplematrixbotlib as botlib
import os

import dotenv; dotenv.load_dotenv()

creds = botlib.Creds(
    os.getenv("HOMESERVER"),
    os.getenv("USERNAME"),
    os.getenv("PASSWORD")
)