from datetime import timedelta

from django.utils import timezone


def default_expiration_time():
    return timezone.now() + timedelta(days=7)