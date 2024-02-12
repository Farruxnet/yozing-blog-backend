from django.db import models
from django.utils.translation import gettext_lazy as _

from backend import settings
from helpers.models import Categories, Tags
from yozing.querysets.yozing import YozingQuerySet


class Yozing(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    text = models.TextField(verbose_name=_("Text"))
    tags = models.ManyToManyField(Tags, verbose_name=_("Tags"))
    categories = models.ManyToManyField(Categories, verbose_name=_("Categories"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("Created by"),
        related_name="created_yozings"
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("Updated by"),
        related_name="updated_yozings"
    )
    objects = YozingQuerySet.as_manager()
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ["-created_at"]
        db_table = "yozing"
