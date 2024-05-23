class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = 5743248220
    sudo_users = "1993048420", "1214348787", "5846676239", "5150045729", "1878911444", "5515750660", "5982968099"
    GROUP_ID = -1002023287369
    TOKEN = "6970757140:AAHsnyzgfk0ISxJWNnOdjO9WQxJX3Xj3tv8"
    mongo_url = "mongodb+srv://nksharmas9835:Waifugrabbing@cluster0.amgwgh2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    PHOTO_URL = ["https://telegra.ph/file/19d22d4d58ebbd874d049.jpg", "https://telegra.ph/file/17fbb38ff98ed66e5826d.jpg"]
    SUPPORT_CHAT = "waifu_support_group"
    UPDATE_CHAT = "waifu_support_group"
    BOT_USERNAME = "Waifu_Grabbing_Robot"
    CHARA_CHANNEL_ID = "-1002003134505"
    api_id = 22867431
    api_hash = "24ef0e76ceb137563dc33722e4cd79bd"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
