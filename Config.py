import os
from dotenv import load_dotenv

load_dotenv()


BOT_TOKEN = os.getenv("BOT_TOKEN")


FORBIDDEN_WORDS = ["so'kinish1", "so'kinish2", "yomonso'z"]


PUNISHMENT_DURATIONS = {
    1: 30,
    2: 90,
    3: 36,
    4: 86
}


VIOLATION_WINDOW = 86400

# Message templates
BLOCKED_MESSAGE_TEMPLATE = """❌ Siz taqiqlangan so'z ishlatdingiz!

🚫 Sabab: "{word}" so'zi taqiqlangan
⏱ Blok muddati: {duration}
📊 Bugungi kunlik buzishlar soni: {count}/4

Iltimos, guruh qoidalariga rioya qiling."""

GROUP_NOTIFICATION_TEMPLATE = """🚫 **Foydalanuvchi bloklandi**

👤 Foydalanuvchi: [{user_name}](tg://user?id={user_id}) `#{user_id}`
🚫 Sabab: "{word}" so'zi ishlatildi
⏱ Blok muddati: {duration}
📊 Bu foydalanuvchining {count}-chi buzishi

_Bu xabar foydalanuvchi blokdan chiqgach o'chadi._"""

def format_duration(seconds):
    if seconds < 60:
        return f"{seconds} soniya"
    elif seconds < 3600:
        minutes = seconds // 60
        return f"{minutes} daqiqa"
    elif seconds < 86400:
        hours = seconds // 3600
        return f"{hours} soat"
    else:
        days = seconds // 86400
        return f"{days} kun"