# (c) github - @IllegalDeveloper ,telegram - https://telegram.me/illegal_Developer
# removing credits doesn't make you coder 


import os
import re

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class Config(object):
    ID = {}
    IS_STREAM = is_enabled('IS_STREAM', True)
    BIN_CHANNEL = int(os.environ.get("BIN_CHANNEL", "-1001896983424"))
    URL = os.environ.get("URL", "https://dashboard.heroku.com/apps/folesj/")
    API_ID = int(os.environ.get("API_ID", "977080"))
    API_HASH = os.environ.get("API_HASH", "0c20c4265501492a1513f91755acd42b")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5991682088:AAFArp6xqU0vY52Lgo4YTy7Y65Dwvli3ACY")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "thunder_store3_bot")
    DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001896983424"))
    SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "instantlinks.co")
    SHORTLINK_API = os.environ.get('SHORTLINK_API', "769114c9c5110bdd01ca6b3e77d651ccc29f5ea0")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "399726799"))
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://abcd:abcd@cluster0.zglig1z.mongodb.net/?retryWrites=true&w=majority")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001336576681")
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1001896983424") 
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
    FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
    OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))   
    SAVE_TO_GALLERY = bool(os.environ.get("SAVE_TO_GALLERY", False))       
    VR_SITE = os.environ.get('VR_SITE', "ziplinker.net")
    VR_API = os.environ.get('VR_API', "37752ccfafb8030f3614dd384405293d5a629203")
    VERIFY = is_enabled((os.environ.get('VERIFY', "True")), True)    
    VERIFY_TXT = """Hey {},
    
ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴠᴇʀɪғɪᴇᴅ ᴛᴏᴅᴀʏ. ᴘʟᴇᴀsᴇ ᴠᴇʀɪғʏ ᴀɴᴅ ɢᴇᴛ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ғᴏʀ ᴏɴᴇ ᴅᴀʏ

<b>ಇಂದು ನೀವು verify ಮಾಡಿಲ್ಲ.. ಆದ ಕಾರಣ ಕೆಳಗಿರುವ ಲಿಂಕ್ ಅನ್ನು ಒತ್ತಿ verify ಮಾಡಿ indu ರಾತ್ರಿ 12am ತನಕ unlimited ಉಚಿತವಾಗಿ movie ಗಳನ್ನ ಪಡೆಯಿರಿ

<b>इस बॉट को इस्तेमाल करने के लिए आपको रोजाना 1 बार verify करना होगा नहीं तो आप इसका इस्तेमाल नहीं कर पाएंगे"""
    VERIFY_COMPLETE_TEXT = """Hey. {}.

ʏᴏᴜ ᴀʀᴇ ɴᴏᴡ ᴠᴇʀɪғɪᴇᴅ ғᴏʀ ᴛᴏɴɪɢʜᴛ 12:00ᴀᴍ ... ᴇɴɪᴏʏ ʏᴏᴜʀ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ғᴏʀ ʏᴏᴜʀ ᴇɴᴛᴇʀᴛᴀɪɴᴍᴇɴᴛ🧑‍🎤 ...

#Completed"""    
    ABOUT_BOT_TEXT = f"""
<b>This is a Permanent FileStore Bot By Illegal Developer.</b>

╭────[ <b>🔅Fɪʟᴇ Sᴛᴏʀᴇ Bᴏᴛ🔅</b>────⍟
│
├🔸 <b>My Name:</b> <a href='https://t.me/{BOT_USERNAME}'>FileStore Bot</a>
│
├🔸 <b>Language:</b> Python 3
│
├🔹 <b>Library:</b> Pyrogram
│
├🔹 <b>Hosted On:</b> Heroku
│
├🔸 <b>Developer:</b> <a href="https://t.me/illegaldeveloperbot">ILLEGAL DEVELOPER</a>
│
├🔸 <b>Update Channel:</b> <a href="https://t.me/illegal_developer">Update Channel</a>
│
╰──────[ 😎 ]───────────⍟
"""
    ABOUT_DEV_TEXT = f"""
 <b>I Am Super Noob Please Support My Hard Work.</b>
"""
    UPGRADE_TEXT = """<b>Are You A Free User? Then Upgrade Your Plan.
 
 Or Buy Premium Just  ₹30 or $ 0.55 And Use the Available Shortner Sites or Can Request Sites.
 
 You can Pay Using Upi Id 
 
 After Doing Payment Send Screenshots Of Payment To Admin"""
    
    UPI_TEXT = """<b>👋 ʜᴇʏ [{}](tg://user?id={})
    
⚜️ ᴘᴀʏ ᴀᴍᴍᴏᴜɴᴛ ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ʏᴏᴜʀ ᴘʟᴀɴ ᴀɴᴅ ᴇɴᴊᴏʏ ᴘʀᴇᴍɪᴜᴍ ᴍᴇᴍʙᴇʀꜱʜɪᴘ !

💵 ᴜᴘɪ ɪᴅ - <code>illegal.developer@axl</code>

‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.</b>"""
    
    PAYPAL_TEXT = """<b>👋 Hey Sweetheart,
 
 ⚜️ Pay Amount According To Your Plan And Enjoy Premium Membership 🤠
 
 🏦 PayPal Id - <spoiler>illegaldeveloper76@gmail.com</spoiler>
 
 📌 Note :- <i>If You Are From a Country Outside India Then Pay Using PayPal</i></b>"""
    
    KO_TEXT = """<b><u>Buy Me A Cup of Coffee</u> ☕
 
 Click Below Button To Buy Coffee And Get Some Peace</b>"""
    
    HOME_TEXT = """
Hello, {},\n\nThis is a Permanent <b>FileStore Bot</b>.

<b><u>How to Use Bot & it's Benefits??</b></u>

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from <b>CopyRight Infringement</b> Issue. I support Channel Also You Can Check <b>About Bot.</b>

❌ <b>PORNOGRAPHY CONTENTS</b> are strictly prohibited & get Permanent Ban..
"""

