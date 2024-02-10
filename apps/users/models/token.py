from datetime import timedelta

from django.conf import settings
from django.db import models
from django.utils import timezone
import jwt

from users.helpers.helpers import default_expiration_time
from users.models.user import User
from django.utils.translation import gettext_lazy as _


class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user', verbose_name=_('User'))
    jwt = models.CharField(max_length=512, unique=True, verbose_name=_('JWT'))
    jwt_expires = models.DateTimeField(
        default=default_expiration_time,
        verbose_name=_('JWT Expires')
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    def __str__(self):
        return f'{self.user}'

    def save(self, *args, **kwargs):
        if not self.jwt:
            self.jwt = self._generate_jwt
        super(Token, self).save(*args, **kwargs)

    @property
    def _generate_jwt(self):
        exp_date = timezone.now() + timedelta(days=30)
        token = jwt.encode(
            payload={"token_type": "access", "user_id": self.user.id, "exp": exp_date},
            key=settings.SECRET_KEY,
            algorithm="HS256"
        )
        return token

    class Meta:
        db_table = 'jwt_tokens'
        verbose_name = _('Token')
        verbose_name_plural = _('Tokens')
        ordering = ('-id',)
