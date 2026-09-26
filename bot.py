import os
import requests
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

SOURCE_CHANNEL = "https://t.me/AjaNews"


def get_news():
    url = "https://t.me/s/AjaNews"
    response = requests.get(url, timeout=20)
    response.raise_for_status()
    return response.text


def main():
    if not BOT_TOKEN or not CHANNEL_ID:
        raise ValueError("BOT_TOKEN أو CHANNEL_ID غير موجود")

    html = get_news()

    print("تم الاتصال بمصدر الأخبار بنجاح")
    print(f"حجم الصفحة: {len(html)}")

    bot = Bot(token=BOT_TOKEN)

    bot.send_message(
        chat_id=CHANNEL_ID,
        text="✅ تم تشغيل NewsPulseYemenBot بنجاح."
    )

    print("تم إرسال رسالة الاختبار إلى القناة")


if __name__ == "__main__":
    main()
