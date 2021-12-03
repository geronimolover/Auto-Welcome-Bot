import os
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import random
import asyncio

Pr0fess0r_99= Client(
    "Welcome-Bot",
     bot_token = os.environ["BOT_TOKEN"],
     api_id = int(os.environ["API_ID"]),
     api_hash = os.environ["API_HASH"]
)

PHOTO = [
    "https://te.legra.ph/file/0acd7e128c2769881823b.png",
    "https://te.legra.ph/file/c3b1ba5faf6f8a67f00db.png",
    "https://telegra.ph/Geronimo-10-28",
    "https://te.legra.ph/file/6e9c01e4773340ce306df.png"
]

@Pr0fess0r_99.on_message(filters.command("start"))
async def start(client: Pr0fess0r_99, update):
    start_msg = "👋Hai {msg.from_user.mention} , Iam Simple Auto Welcome Bot"
    bot_username = await client.get_me()
    link = "PR0FESS0R-99/Auto-Welcome-Bot"
    reply_markup = InlineKeyboardMarkup(
        [             
            [
                InlineKeyboardButton
                    (
                         "Channel", url="t.me/free_music123"
                    ),
                InlineKeyboardButton
                    (
                         "Group", url="t.me/all_super_movies"
                    )
            ],   
            [
                InlineKeyboardButton
                   (
                        "Status", url=f"http://t.me/all_super_status"
                   )
            ]
        ] 
    )                       
    await update.reply_photo(
    photo=f"{random.choice(PHOTO)}",
    caption="👋Hey,\nIam Moscow\n\nI greet new members in my group\nI cant work in your group\n\nSee you in @all_super_movies",
    parse_mode="html",
    reply_markup = reply_markup    
)



@Pr0fess0r_99.on_message(filters.private & filters.command("admin"))
async def admin(bot: Pr0fess0r_99, update):
    # Heroku Support
    user = "👋Hey {}, \n You cant command me!"
    run = "WxJ3G7NBb4c" # https://github.com/PR0FESS0R-99/Auto-Welcome-Bot
    api_key = os.environ.get("APP_NAME", "AutoWelcomeBot")
    DEPLOY = bool(os.environ.get("HOSTED"))
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "").split())
    if not DEPLOY:
       reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton
                    (
                        "⚙️No SETTINGS⚙️", url=f"https://google.com"
                    )
            ]
        ]
    )
    else:
       reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton
                    (
                        "⚙️no APP⚙️", url="https://google.com"
                    )
            ]
        ]
    )
    if not DEPLOY:
       user_admin = "Open Heroku => Application => Settings => Config Vars => Welcome_Text Edit"
    else:
       user_admin = "Open Railway Website=> Application => Variables => Welcome_Text Edit"
    deploy =InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton
                    (
                        "💫 GROUP 💫", url=f"https://t.me/all_super_movies"
                    )
            ]
        ]
    )
    if update.from_user.id not in OWNER_ID:
        await update.reply_text(text=user.format(update.from_user.mention), reply_markup=deploy)
        return
    await update.reply_text(text=user_admin, reply_markup=reply_markup)

@Pr0fess0r_99.on_message(filters.new_chat_members)
async def auto_welcome(bot: Pr0fess0r_99, msg: Message):
    # from PR0FESS0R-99 import ID-Bot
    first = msg.from_user.first_name
    last = msg.from_user.last_name
    mention = msg.from_user.mention
    username = msg.from_user.username
    id = msg.from_user.id
    group_name = msg.chat.title
    group_username = msg.chat.username
    name_button = "🔰 JOIN NOW 🔰"
    link_button = "t.me/Mo_tech_YT"
    button_name = os.environ.get("WELCOME_BUTTON_NAME", name_button)
    button_link = os.environ.get("WELCOME_BUTTON_LINK", link_button)
    welcome_text = f"Hey {mention}\nWelcome To {group_name}"
    WELCOME_TEXT = os.environ.get("WELCOME_TEXT", welcome_text)
    print("Welcome Message Activate")
    BUTTON = bool(os.environ.get("WELCOME_BUTTON"))
    if not BUTTON:
       k = await msg.reply_text(text=WELCOME_TEXT.format(
           first = msg.from_user.first_name,
           last = msg.from_user.last_name,
           username = None if not msg.from_user.username else '@' + msg.from_user.username,
           mention = msg.from_user.mention,
           id = msg.from_user.id,
           group_name = msg.chat.title,
           group_username = None if not msg.chat.username else '@' + msg.chat.username
          ),
       reply_markup=InlineKeyboardMarkup(
               [
                   [
                       InlineKeyboardButton
                           (
                               button_name, url=button_link
                           )
                   ]  
               ]
           )
       )  
       await asyncio.sleep(5)
       await k.delete()

print("""Auto Welcome Bot Started

Maintained By @Mo_Tech_YT""")

Pr0fess0r_99.run()
