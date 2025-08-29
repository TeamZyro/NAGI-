import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "28615030"))
API_HASH = getenv("API_HASH", "4cd09b1bcd45560ee35e8be593f13d83")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7898735839:AAFWtOAXTh7qRew_Jvh4YAiXT0uK2hLH9O8")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv(
    "MONGO_DB_URI",
    "mongodb+srv://kafka:kafka@cluster0.z4xolqj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)

# Duration limit in minutes (int)
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 10000000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -1003084307535))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 6037958673))
DEV_ID = int(getenv("DEV_ID", 6037958673))

# Your custom API URLs and keys for youtube/video APIs:
API_URL = getenv("API_URL", "https://api.thequickearn.xyz")  # VPS Host URL for API
API_KEY = getenv("API_KEY", "30DxNexGenBots48df04")  # API Key for youtube song API

# Fill these variables if you're deploying on Heroku.
# Your Heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

# Upstream repository (e.g. your GitHub repo)
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/sungjinw04/nobaramusic",
)

# Branch of the upstream repo
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

# Git token if your upstream repository is private
GIT_TOKEN = getenv(
    "GIT_TOKEN", "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"
)

# Support channels & chats
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/pookie_updates")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/pookieempire")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# Spotify credentials (from https://developer.spotify.com/dashboard)
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "6be9f0b34c384ad097cc71b1c1fc5e8b")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "2607415f99944cc6b24fa98018fb8c09")

# Maximum limit for fetching playlist's tracks from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 50000))

# Telegram audio and video file size limits (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))  # 100MB
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))  # 1GB

    # ========================== APIs ========================== #
BASE_API_URL = "https://zyro.zyronetworks.shop"
BASE_API_KEY = "mTp6fyc98WzSd7EYK7edQMXPf8VZrfxk"

# Get your pyrogram v2 sessions from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION1", "BQFYNJ4ASWRikT3YXtoHKYMoI3o4WIWHh2py3x1QTGe3MWhW7-ghUxYNcZ_1Fe1dTFatCU_gW4xSibZQOB2SOKdHH5VnWs1oHeObeP_lHVkyuOV2qGotUdWM_dNNfJmRevAcsr5HHzM87Pislsto6o2YQuNjiRGbR2-J7uLsxPysDcEnp1m0RQwxIRQrsHggKXoAQ2Fl1jPAE9PWgov4Qnz6rjdQshWsfXL7cWF5Jjj240brDX4cCCeHrp-pUKH-XPWEIZS2lkxGqVkxkR2MqyKG-1V4fUXRcCBbu0-Ao5Wy-qp2_T4YdWq8TZLsjPWvcnHHUH-dzt5RXaiat2sgvA9REEiPfAAAAAHnX8XRAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

# Filters and global vars
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# Default images and URLs used by the bot
START_IMG_URL = getenv("START_IMG_URL", "https://files.catbox.moe/owdeng.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://files.catbox.moe/w6x79m.jpg")
PLAYLIST_IMG_URL = "https://envs.sh/JV-.jpg"
STATS_IMG_URL = "https://files.catbox.moe/rzmojl.jpg"
TELEGRAM_AUDIO_URL = "https://envs.sh/JV-.jpg"
TELEGRAM_VIDEO_URL = "https://envs.sh/JVx.jpg"
STREAM_IMG_URL = "https://envs.sh/JV-.jpg"
SOUNCLOUD_IMG_URL = "https://envs.sh/JVx.jpg"
YOUTUBE_IMG_URL = "https://envs.sh/JV-.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://envs.sh/JVx.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://envs.sh/JV-.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://envs.sh/JVx.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match(r"(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match(r"(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )

