from django.conf import settings
import telebot

bot = telebot.TeleBot(settings.BOT_TOKEN)
