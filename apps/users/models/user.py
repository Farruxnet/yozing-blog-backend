from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.helpers.managers import UserManager


class User(AbstractUser):
    username = models.CharField(max_length=32, unique=True, null=True, blank=True, verbose_name=_('Username'))
    full_name = models.CharField(max_length=64, blank=True, null=True, verbose_name=_('Full name'))
    password = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("Password"))
    email = models.EmailField(unique=True, max_length=128, blank=True, verbose_name=_('Email'))
    telegram_id = models.BigIntegerField(default=0, verbose_name=_('Telegram'))
    image = models.ImageField(upload_to='users/', null=True, blank=True, verbose_name=_('Image'))
    phone_number = models.CharField(max_length=12, unique=True, null=True, blank=True, verbose_name=_('Phone number'))

    linkedin_url = models.URLField(null=True, blank=True, verbose_name=_('Linkedin'))
    github_url = models.URLField(null=True, blank=True, verbose_name=_('Github'))
    instagram_url = models.URLField(null=True, blank=True, verbose_name=_('Instagram'))
    facebook_url = models.URLField(null=True, blank=True, verbose_name=_('Facebook'))

    is_active = models.BooleanField(default=True, verbose_name=_('Is active?'))
    is_staff = models.BooleanField(default=False, verbose_name=_('Is staff?'))
    is_admin = models.BooleanField(default=False, verbose_name=_('Is superuser?'))
    is_superuser = models.BooleanField(default=False, verbose_name=_('Is superuser?'))
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name=_('Date joined'))

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        db_table = 'users'
        ordering = ['-id']
