from django.contrib import admin

from users.models import User
from . models import Yozing


@admin.register(Yozing)
class YozingAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'updated_at']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'updated_by':
            kwargs["initial"] = request.user.id
            kwargs["queryset"] = User.objects.filter(id=request.user.id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
