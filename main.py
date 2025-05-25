# main.py
from aiogram import Bot, Dispatcher, executor, types
import logging
import os
from services import generate_assignment, generate_invite, generate_business_card, generate_course_outline

API_TOKEN = "7615857848:AAEoJyFBCI4KWKeor52y0LBEmGYI29-t3WI"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    await message.reply("Assalomu alaykum! Xizmat turini tanlang:\n1. Mustaqil ish\n2. Vizitka dizayni\n3. Video kurs\n4. To'y taklifnomasi")

@dp.message_handler(lambda message: message.text.strip().isdigit())
async def service_selector(message: types.Message):
    services = {
        "1": generate_assignment,
        "2": generate_business_card,
        "3": generate_course_outline,
        "4": generate_invite
    }
    await message.reply("Iltimos, mavzuni kiriting:")
    dp.register_message_handler(lambda msg: handle_service(msg, services[message.text.strip()]), content_types=types.ContentTypes.TEXT, state=None)

async def handle_service(message, service_function):
    result = service_function(message.text)
    await message.reply(result)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)