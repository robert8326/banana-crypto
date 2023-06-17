from typing import Optional

from rest_framework.permissions import IsAuthenticated

from apps.user.models import User


class IsTelegramUser(IsAuthenticated):
    def has_permission(self, request, view) -> bool:
        if request.method == 'POST':
            telegram_id: Optional[int] = request.data.get('telegram_id')
            if telegram_id:
                return User.objects.filter(telegram_id=telegram_id).exists()
        elif request.method == 'GET':
            telegram_id: Optional[int] = request.query_params.get('telegram_id')
            if telegram_id:
                return User.objects.filter(telegram_id=telegram_id).exists()
        return super().has_permission(request, view)
