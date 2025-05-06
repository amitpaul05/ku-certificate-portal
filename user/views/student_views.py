from rest_framework.generics import ListCreateAPIView

from user.models import Student
from user.serializers.student_serializers import StudentSerializer


class StudentListView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer