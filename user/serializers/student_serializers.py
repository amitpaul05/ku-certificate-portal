from rest_framework import serializers
from django_countries.serializer_fields import CountryField
from user.models import Student

class StudentSerializer(serializers.ModelSerializer):
    nationality = CountryField()

    class Meta:
        model = Student
        fields = '__all__'
