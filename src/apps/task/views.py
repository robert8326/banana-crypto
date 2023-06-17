from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import IsAuthenticated

from apps.task.models import Task
from apps.task.serializers import TaskSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer
    http_method_names = ('post', 'get', 'patch', 'delete')

    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset()
        return queryset.filter(user=user)
