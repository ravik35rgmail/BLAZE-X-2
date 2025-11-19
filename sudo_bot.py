from pyrogram import Client, filters
from pyrogram.types import Message
from itertools import cycle
from data import RAID, REPLYRAID, PORMS, MRAID, SRAID, CRAID

# Common API ID and HASH for all bots
API_ID = 27093880
API_HASH = "03ab44fe40af4c9a87ebf9f866bddf4a"

# Your sudo users
SUDO_USERS = [6181216007, 6160198652, 8133353056, 6577424999, 7096797675, 7905609750, 8019020221, 8128202671, 8026269436, 7565596497, 6013815906, 7035572021, 7961741937, 7736279090, 5148621690, 8119245009, 8340675844, 7629925573, 8258688313, 8473392583, 6673008256, 6309067514]

# Predefined command map
COMMAND_MAP = {
    "raid": cycle(RAID),
    "replyraid": cycle(REPLYRAID),
    "porm": cycle(PORMS),
    "mraid": cycle(MRAID),
    "sraid": cycle(SRAID),
    "craid": cycle(CRAID)
}

# List of your 10 bots, add token in this format
bots = [
    {"name": "ʙʟᴀᴢᴇ_ғɪɢʜᴛᴇʀ𝟶𝟷", "bot_token": "7685199221:AAFEWdFj31e033R7KW09iH0v6LvCer-pS_0"},
    {"name": "ʙʟᴀᴢᴇ_ғɪɢʜᴛᴇʀ𝟶𝟸", "bot_token": "8008359217:AAHM_WtV6ZMbLp6euLzDKKiXAm1wcQlXr8Q"},
    {"name": "ʙʟᴀᴢᴇ_ғɪɢʜᴛᴇʀ𝟶𝟹", "bot_token": "7640093843:AAEYeyg6pmPbMCLqxX8GmDxwOPIOmRuwLps"},
    {"name": "ʙʟᴀᴢᴇ_ғɪɢʜᴛᴇʀ𝟶𝟺", "bot_token": "7053202288:AAF5-_Uf2hxishtM1rW3rEp_JDrQLTXG90Y"},
    {"name": "ʙʟᴀᴢᴇ_ғɪɢʜᴛᴇʀ𝟶𝟻", "bot_token": "7359950563:AAHV3lMZvZtYbUJrjHGaDlCM7-S6a1Ls9G4"},
    {"name": "ʙʟᴀᴢᴇ_ғɪɢʜᴛᴇʀ𝟶𝟼", "bot_token": "8166557365:AAH28q7RBQIsTN0hzzigBCP7zaRwds_kihI"},
    {"name": "ʙʟᴀᴢᴇ_ғɪɢʜᴛᴇʀ𝟶𝟽", "bot_token": "7398309381:AAHbiVwS7Ddx0K0AJkpOFWy1S4yHyQJimB4"},
    {"name": "ʙʟᴀᴢᴇ_ғɪɢʜᴛᴇʀ𝟶𝟾", "bot_token": "7598643740:AAFOQJMVnDDYUrKRDBPHBvJVAx-b-jLlBiY"},
    {"name": "ʙʟᴀᴢᴇ_ғɪɢʜᴛᴇʀ𝟶𝟿", "bot_token": "7550990971:AAGcVXq2GLz_0cL3gszJcN1LPqElpU2c4Xg"},
    {"name": "ʙʟᴀᴢᴇ_ғɪɢʜᴛᴇʀ𝟷𝟶", "bot_token": "7913551854:AAH1qCmOhzaLfghjf9vEprAyJR2VF8Z5-7Q"},
]

clients = []

def get_target(message):
    if message.reply_to_message:
        return message.reply_to_message.from_user.mention
    parts = message.text.split()
    if len(parts) >= 3:
        return parts[2]
    return None

def create_handler(app, command):
    cycle_list = COMMAND_MAP[command]

    @app.on_message(filters.command(command, prefixes=".") & (filters.group | filters.private))
    def handler(client, message: Message):
        if message.from_user.id not in SUDO_USERS:
            return message.reply("❌ Not allowed.")
        parts = message.text.split()
        if len(parts) < 2:
            return message.reply(f"Usage: .{command} <count> [@username or reply]")
        try:
            count = int(parts[1])
            if count > 1000:
                return message.reply("⚠️ Max 100 messages allowed.")
        except ValueError:
            return message.reply("❌ Invalid count number.")

        target = get_target(message)
        if not target:
            return message.reply("❌ Please mention or reply to a user.")

        for _ in range(count):
            try:
                message.reply_text(f"{target}\n\n{next(cycle_list)}")
            except Exception as e:
                print("Error:", e)
        message.reply("✅ Raid completed.")

def add_ping_handler(app):
    @app.on_message(filters.command("ping", prefixes="/") & (filters.group | filters.private))
    def ping_handler(client, message: Message):
        if message.from_user.id in SUDO_USERS:
            message.reply("ʙᴏᴛ ɪs ᴀʟɪᴠᴇ ʙᴀʙʏ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴅʀᴀɢᴏɴ ғᴀᴛʜᴇʀ. ❤‍🔥")

# Initialize bots
for bot in bots:
    if not bot["bot_token"]:
        print(f"⚠️ Skipping {bot['name']}, no token provided.")
        continue

    app = Client(
        name=bot["name"],
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=bot["bot_token"]
    )

    for cmd in COMMAND_MAP:
        create_handler(app, cmd)
    add_ping_handler(app)

    clients.append(app)

# Start all clients
for client in clients:
    client.start()

print("✅ All bots are now running.")
import asyncio
asyncio.get_event_loop().run_forever()