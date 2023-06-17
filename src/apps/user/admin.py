from django.contrib import admin

from apps.user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'is_telegram_user', 'date_joined', 'is_superuser')
    fields = ('username', 'is_telegram_user', 'date_joined', 'is_superuser',)
    readonly_fields = ('date_joined', 'is_superuser', 'is_telegram_user')
