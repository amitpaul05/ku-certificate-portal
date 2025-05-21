from rest_framework import serializers
import uuid
from form.models import ApplyForm, Payment
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

    def create(self, validated_data):
        student = validated_data['student']

        # Create the ApplyForm
        apply_form = ApplyForm.objects.create(**validated_data)

        # Create the Payment with dummy transaction_id
        Payment.objects.create(
            student=student,
            transaction_id=f"TX-{uuid.uuid4().hex[:8]}",  # e.g., "demo-a1b2c3d4"
            form=apply_form
        )

        # Set is_paid to True
        apply_form.is_paid = True
        apply_form.save()

        return apply_form



class HeadApproveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplyForm
        fields = '__all__'
        read_only_fields = (
            'id', 'is_paid', 'is_dsa_approved', 'is_librarian_approved', 'librarian_approved_by',
            'dsa_approved_by','is_provost_approved', 'provost_approved_by', 'degree', 'cgpa', 'total_credit', 'earned_credit', 'date_of_last_exam', 'student', 'discipline', 'hall'
        )



class DsaApproveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplyForm
        fields = '__all__'
        read_only_fields = (
            'id', 'is_paid','is_head_approved', 'is_librarian_approved', 'librarian_approved_by',
            'is_provost_approved', 'provost_approved_by',
            'head_approved_by', 'degree', 'cgpa', 'total_credit', 'earned_credit', 'date_of_last_exam', 'student', 'discipline', 'hall'
        )


class LibrarianApproveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplyForm
        fields = '__all__'
        read_only_fields = (
            'id', 'is_paid', 'is_head_approved', 'is_dsa_approved', 'dsa_approved_by',
            'head_approved_by', 'is_provost_approved', 'provost_approved_by', 'degree', 'cgpa', 'total_credit', 'earned_credit', 'date_of_last_exam', 'student', 'discipline', 'hall'
        )


class ProvostApproveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplyForm
        fields = '__all__'
        read_only_fields = (
            'id', 'is_paid', 'is_head_approved', 'is_dsa_approved', 'dsa_approved_by',
            'head_approved_by', 'is_librarian_approved', 'librarian_approved_by', 'degree', 'cgpa', 'total_credit', 'earned_credit', 'date_of_last_exam', 'student', 'discipline', 'hall'
        )