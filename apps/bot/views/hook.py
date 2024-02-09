from django.http import JsonResponse
from telebot import types
from bot.helpers.bot import bot


def hook(request):
    if request.method == 'POST':
        bot.process_new_updates([types.Update.de_json(request.body.decode('utf-8'))])
        return JsonResponse({'success': True}, status=200)
    return JsonResponse({'success': False}, status=405)


