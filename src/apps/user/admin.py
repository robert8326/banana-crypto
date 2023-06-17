from django.contrib import admin

from apps.user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'date_joined', 'is_superuser')
    fields = ('username', 'date_joined', 'telegram_id', 'is_superuser',)
    readonly_fields = ('date_joined', 'is_superuser')
