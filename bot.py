import os
import django
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from asgiref.sync import sync_to_async

# Django konfiguratsiyasini o'rnating
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Config.settings')
django.setup()

# Django modellarini import qiling
from phones.models import Phone, Purchase

API_TOKEN = '6401855105:AAGUkgOmQzVCt91hsHVwyRyI4ez3V19bx5o'  # O'z bot tokeningizni bu yerga yozing

# Bot va Dispatcher ni yarating
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Default telefonlar ro'yhati
default_phones = [
    {'model': 'iPhone 11', 'price': 700.00},
    {'model': 'iPhone 11 Pro', 'price': 900.00},
]


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Salom! Telefonlarni ko'rish uchun /telefonlar yozing.")


@dp.message_handler(commands=['telefonlar'])
async def show_phone_list(message: types.Message):
    if not default_phones:
        await message.answer("Hozircha telefonlar yo'q.")
    else:
        # Default telefonlar ro'yhatini foydalanuvchiga ko'rsatish
        for phone in default_phones:
            text = f"Model: {phone['model']}\nNarxi: {phone['price']} so'm\n"
            # Sotib olish uchun inline button
            keyboard = InlineKeyboardMarkup().add(
                InlineKeyboardButton('Sotib olish', callback_data=f'buy_{phone["model"]}'))
            await message.answer(text, reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data.startswith('buy_'))
async def process_buy(callback_query: types.CallbackQuery):
    phone_model = callback_query.data.split('_')[1]
    await bot.answer_callback_query(callback_query.id)

    # Foydalanuvchidan ism so'raymiz
    await bot.send_message(callback_query.from_user.id, f"{phone_model} ni sotib olish uchun ismingizni kiriting:")
    await dp.current_state(user=callback_query.from_user.id).set_state("waiting_for_name")
    await dp.current_state(user=callback_query.from_user.id).update_data(phone_model=phone_model)


@dp.message_handler(state="waiting_for_name")
async def process_name(message: types.Message):
    user_name = message.text
    await dp.current_state(user=message.from_user.id).update_data(name=user_name)
    await message.answer(f"{user_name}, endi telefon raqamingizni kiriting:")
    await dp.current_state(user=message.from_user.id).set_state("waiting_for_phone")


@dp.message_handler(state="waiting_for_phone")
async def process_phone(message: types.Message):
    user_phone = message.text
    user_data = await dp.current_state(user=message.from_user.id).get_data()

    user_name = user_data.get("name")
    phone_model = user_data.get("phone_model")

    # Telefon modelini olish
    phone = await sync_to_async(Phone.objects.get)(model=phone_model)

    # Sotib olish ma'lumotlarini saqlash
    purchase = Purchase(phone=phone, buyer_name=user_name, buyer_phone=user_phone)
    await sync_to_async(purchase.save)()

    await message.answer(f"Sizning telefon raqamingiz: {user_phone}\nSiz muvaffaqiyatli sotib oldingiz!")

    # Davom etish
    await dp.current_state(user=message.from_user.id).finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
