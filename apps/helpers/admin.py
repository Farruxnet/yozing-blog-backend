from django.contrib import admin
from .models import Contacts, Tags, About, Rules, Categories


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if Contacts.objects.exists():
            return False
        return True


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    pass


@admin.register(About)
class AboutsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if About.objects.exists():
            return False
        return True


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    pass


@admin.register(Rules)
class RulesAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if Rules.objects.exists():
            return False
        return True
