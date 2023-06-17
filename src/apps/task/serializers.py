from rest_framework.serializers import ModelSerializer

from apps.task.models import Task


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'user', 'header', 'description', 'completed',)
        extra_kwargs = {
            'user': {'read_only': True}
        }

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super(TaskSerializer, self).create(validated_data)
