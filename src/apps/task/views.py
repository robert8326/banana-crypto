from rest_framework.viewsets import ModelViewSet

from apps.task.models import Task
from apps.task.serializers import TaskSerializer
from apps.user.models import User
from apps.user.permissions import IsTelegramUser


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = (IsTelegramUser,)
    serializer_class = TaskSerializer
    http_method_names = ('post', 'get', 'patch', 'delete')

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            user = self.request.user
        else:
            user = User.objects.get(telegram_id=self.request.query_params.get('telegram_id'))
        return queryset.filter(user=user)
