from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.task.views import TaskViewSet

router = DefaultRouter()
router.register('task', TaskViewSet)

urlpatterns = []
urlpatterns += router.urls
