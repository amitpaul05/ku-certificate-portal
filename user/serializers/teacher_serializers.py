from rest_framework import serializers
from user.models import Teacher

class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)

        # Check Head role
        head = instance.heads.order_by('-start_date').first()
        if head:
            data['head_info'] = {
                "discipline": head.discipline.id,
                "start_date": head.start_date,
                "end_date": head.end_date,
            }
            return data

        # Check DSA role
        dsa = getattr(instance, 'dsa', None)
        if dsa:
            data['dsa_info'] = {
                "start_date": dsa.start_date,
                "end_date": dsa.end_date,
            }
            return data

        # Check Provost role
        provost = getattr(instance, 'provost', None)
        if provost:
            data['provost_info'] = {
                "start_date": provost.start_date,
                "end_date": provost.end_date,
                "hall": provost.hall.id,
            }
            return data

        return data