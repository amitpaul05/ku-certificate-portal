from rest_framework import serializers
from user.serializers.teacher_serializers import TeacherSerializer

from hall.models import Provost


class ProvostSerializer(serializers.ModelSerializer):
    teacher_details = TeacherSerializer(source='teacher', many=False, read_only=True)
    class Meta:
        model = Provost
        fields = '__all__'