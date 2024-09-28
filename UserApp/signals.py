import requests
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UsersInfoModel
import os

@receiver(post_save, sender=UsersInfoModel)
def send_telegram_notification(sender, instance, *args, **kwargs):
    bot_token = '6401855105:AAGUkgOmQzVCt91hsHVwyRyI4ez3V19bx5o'
    chat_id = '1091591701'

    # SQLite fayl yo'li
    sqlite_file_path = os.path.join(os.getcwd(), 'db.sqlite3')

    # Fayl mavjudligini tekshirish
    if not os.path.exists(sqlite_file_path):
        print(f"SQLite fayli topilmadi: {sqlite_file_path}")
        return

  
    # Yangi qo'shilgan ma'lumot caption sifatida
    caption = (f"👥 New user created\n"
               f"👤 Username: {instance.username}\n"
               f"👤 Full Name: {instance.first_name} {instance.last_name}\n"
               f"📧 Email: {instance.email}")

    # Faylni yuborish
    url_send_file = f"https://api.telegram.org/bot{bot_token}/sendDocument"
    with open(sqlite_file_path, 'rb') as file:
        response = requests.post(url_send_file, data={'chat_id': chat_id, 'caption': caption}, files={'document': file})

    # Javobni tekshirish
    if response.status_code == 200:
        print("Fayl muvaffaqiyatli yuborildi!")
    else:
        print(f"Fayl yuborishda xatolik: {response.status_code} - {response.text}")
