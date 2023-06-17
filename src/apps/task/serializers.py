from rest_framework.serializers import ModelSerializer
from rest_framework.validators import ValidationError

from apps.task.models import Task
from apps.user.models import User


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'user', 'header', 'description', 'completed',)
        extra_kwargs = {
            'user': {'read_only': True}
        }

    def validate(self, attrs):
        user = self.context['request'].user
        if user.is_anonymous:
            user = User.objects.filter(telegram_id=self.context['request'].data.get('telegram_id'))
            if not user.exists():
                raise ValidationError({'detail': "User with this telegram_id does not exist"})
            user = user.first()
        attrs['user'] = user
        return attrs
