import simplematrixbotlib as botlib

class BlockString:
    def __init__(self, admin_ids: list[str], bot: botlib.Bot, storage_location: str):
        self._admin_ids = admin_ids
        self._bot = bot
        self._storage_location = storage_location
        self.string_blacklist = self.read_blacklist()
        self.commands = [
            ["block_string", "This command adds strings to the blacklist when used by an admin"]
        ]
        self._bot.add_message_listener(self.block_strings)
        self._bot.add_message_listener(self.add_new_blocked_string)
    
    def read_blacklist(self):
        try:
            with open(self._storage_location, 'r') as f:
                return f.read().splitlines()

        except FileNotFoundError:
            with open(self._storage_location, 'w'):
                pass #Create empty file
            return []
    
    def write_blacklist(self):
        with open(self._storage_location, 'r') as f:
            f.writelines(self.string_blacklist)
    
    def is_blocked(self, string: str):
        if string in self.string_blacklist:
            return True
    
    def new_block_string(self, string: str):
        if not self.is_blocked(string):
            self.string_blacklist.append(string)
        self.write_blacklist()
    
    async def block_strings(self, room, message):
        for string in self.string_blacklist:
            if string in message.body:
                await self._bot.api.async_client.room_redact(room.room_id, message.event_id, "Part of this message has been blacklisted.")
    
    async def add_new_blocked_string(self, room, message):
        match = botlib.MessageMatch(room, message, self._bot)

        if match.not_from_this_bot and match.prefix(self._bot.prefix) and match.command("block_string"):
            temp = False
            for id in self._admin_ids:
                if message.sender == id:
                    temp = True
            if not temp:
                await self._bot.api.send_text_message(room.room_id, "This command is admin only.")
                return
            for arg in match.args:
                self.string_blacklist.append(arg)
            self.write_blacklist()