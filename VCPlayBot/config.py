import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("5801366697:AAGYouzDcXwrQoJs0oGKkku6mL4_9Dk42ic")
BOT_NAME = getenv("music BOT")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "LaylaBots")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/9b13ea3ce046a1a5c8098.png")
admins = {}
API_ID = int(getenv("26840920"))
API_HASH = getenv("a90d0f9cc34e615788366636930254b2")
BOT_USERNAME = getenv("musicbotkon_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Dead0XD")
OWNER_NAME = getenv("Owner_name", "𝐁sシ︎sαꪑ 𝐌вāꪶяĸ𝔦")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "tanolnc")
PROJECT_NAME = getenv("PROJECT_NAME", "VCPlayBot2.0")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/QueenArzoo/VCPlayBot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5201596329").split()))
