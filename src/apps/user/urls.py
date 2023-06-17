from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,

)

from apps.user.views import (
    RegisterUserAPIView,
    CheckTelegramUserApiView,
    LoginTelegramUserApiView
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterUserAPIView.as_view(), name='register'),
    path('telegram/<int:telegram_id>/', CheckTelegramUserApiView.as_view(), name='telegram_login'),
    path('telegram/login/', LoginTelegramUserApiView.as_view(), name='telegram_login'),
]
