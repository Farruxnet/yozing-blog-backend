from django.contrib import admin

from users.models import User, Token

admin.AdminSite.site_title = "Yozing.Blog"
admin.AdminSite.site_header = "Yozing.Blog"


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'full_name')


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    readonly_fields = ('jwt', )

