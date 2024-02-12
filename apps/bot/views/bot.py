from django.contrib.auth.hashers import make_password

from bot.helpers.bot import bot
from bot.helpers.random_otp import random_otp
from bot.helpers.redis_db import redis_client, save_otp_to_redis
from users.models import User


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        text="Assalomu alaykum, Yozing.Blog ga login qilish uchun /login buyrug'ini bosing",
        parse_mode='html'
    )


@bot.message_handler(commands=['login'])
def login(message):
    random_ = random_otp()
    save_otp_to_redis(random_otp=random_, message=message)

    full_name = message.chat.first_name

    if message.chat.last_name:
        full_name += ' ' + message.chat.last_name

    User.objects.get_or_create(
        username=message.from_user.username,
        email=f'{message.chat.id}@yozing.blog',
        full_name=full_name,
        telegram_id=message.chat.id
    )

    bot.send_message(
        message.chat.id,
        text=f"OTP: `{random_}`",
        parse_mode='MarkDown'
    )
