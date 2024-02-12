from django.db import models
from django.utils.translation import gettext_lazy as _

from helpers.querysets.category import CategoryQuerySet
from helpers.querysets.tags import TagQuerySet


class Tags(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name=_('Name'))
    objects = TagQuerySet.as_manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')
        ordering = ('name',)
        db_table = 'tags'


class Categories(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name=_('Name'))
    objects = CategoryQuerySet.as_manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ('name',)
        db_table = 'categories'


class Contacts(models.Model):
    description = models.CharField(max_length=512, verbose_name=_('Description'))
    address = models.CharField(max_length=512, verbose_name=_('Address'))
    phone = models.CharField(max_length=20, verbose_name=_('Phone'))
    email = models.EmailField(max_length=128, unique=True, verbose_name=_('Email'))

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')
        db_table = 'contacts'


class About(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name=_('Name'))
    description = models.TextField(verbose_name=_('Description'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('About Page')
        verbose_name_plural = _('About Pages')
        db_table = 'about'


class Rules(models.Model):
    terms_of_use = models.TextField(verbose_name=(_('Terms of Use')))
    privacy_policy = models.TextField(verbose_name=_('Privacy Policy'))
    cookie_policy = models.TextField(verbose_name=_('Cookie Policy'))

    def __str__(self):
        return _("Rules")

    class Meta:
        verbose_name = _("Rule")
        verbose_name_plural = _("Rules")
        db_table = 'rules'
