from userbot.Config import Var
from telethon.sessions import StringSession
from telethon import TelegramClient

# Global Variables
CMD_LIST = {}
CMD_HELP = {}
INT_PLUG = ""
LOAD_PLUG = {}

if Var.STRING_SESSION:
    session_name = str(Var.STRING_SESSION)
    bot = TelegramClient(StringSession(session_name), Var.APP_ID, Var.API_HASH)
else:
    session_name = "startup"
    bot = TelegramClient(session_name, Var.APP_ID, Var.API_HASH)

x = bot.me
name = x.first_name
