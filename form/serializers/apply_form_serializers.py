from rest_framework import serializers

from form.models import ApplyForm
from discipline.serializers.discipline_serializers import DisciplineSerializer
from user.serializers.student_serializers import StudentSerializer
from hall.serializers.hall_serializers import HallSerializer


class ApplyFormSerializer(serializers.ModelSerializer):
    student_details = StudentSerializer(source='student', read_only=True)
    discipline_details = DisciplineSerializer(source='discipline', read_only=True)
    hall_details = HallSerializer(source='hall', read_only=True)
    class Meta:
        model = ApplyForm
        fields = '__all__'
        read_only_fields = (
            'id', 'is_paid', 'is_controller_approved', 'is_dsa_approved', 'is_librarian_approved',
            'is_head_approved', 'head_approved_by', 'librarian_approved_by', 'dsa_approved_by'
        )