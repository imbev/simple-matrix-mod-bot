# Simple Matrix Mod Bot
(Version 0.1.0)

This is a simple moderation bot for [Matrix](matrix.org) rooms made using [Simple-Matrix-Bot-Lib](https://github.com/KrazyKirby99999/simple-matrix-bot-lib) and Python.


## Usage

### Download from github
Download this git repository using the following command:
```bash
git clone https://github.com/KrazyKirby99999/simple-matrix-mod-bot.git
```

### Install dependencies
The python packages needed to run this bot are found in requirements.txt and can be installed using the following command:
```bash
pip install -r requirements.txt
```

### Set variables
There are a number of variables that must be set in order to run the bot. These variables are can be set using a .env file. An example is shown below:
```
HOMESERVER=https://example.com
USERNAME=somebotusername
PASSWORD=somepassword
STORAGE=./.storage/
PREFIX=!
```

### Room setup
For the bot to moderate a room, it must be invited to the room, then be given the admin role. These actions can be reversed using the same credentials that you used earlier.

If you want to be able to use "admin only" commands through the bot, it is neccesary to add your id to the admin_id list found in bot.py .

### Additional changes
Feel free to make changes to bot.py and modules in order to add, remove, and modify features.
