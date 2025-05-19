from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from user.models.user_models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from user.serializers.student_serializers import StudentSerializer
from user.serializers.teacher_serializers import TeacherSerializer
from user.serializers.librarian_serializers import LibrarianSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'gender', 'password', 'id', 'user_type']
        read_only_fields = ['id']
        extra_kwargs = {
            "password": {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
            return instance
        return None

    def to_representation(self, instance):
        data = super().to_representation(instance)
        user_type = instance.user_type

        if user_type == 'student' and hasattr(instance, 'student'):
            data['student_details'] = StudentSerializer(instance.student).data
        elif user_type == 'teacher' and hasattr(instance, 'teachers'):
            data['teacher_details'] = TeacherSerializer(instance.teachers).data
        elif user_type == 'librarian' and hasattr(instance, 'librarians'):
            data['librarian_details'] = LibrarianSerializer(instance.librarians).data

        return data


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['user_id'] = str(user.id)

        if user.user_type == 'student':
            student = getattr(user, 'student', None)
            if student:
                token['student_id'] = str(student.student_id)
            else:
                token['student_id'] = None

        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data['user_id'] = str(self.user.id)

        if self.user.user_type == 'student':
            student = getattr(self.user, 'student', None)
            if student:
                data['student_id'] = str(student.student_id)
            else:
                data['student_id'] = None

        return data
