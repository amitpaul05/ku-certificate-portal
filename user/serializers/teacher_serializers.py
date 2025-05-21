from rest_framework import serializers
from user.models import Teacher

class TeacherDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)

        # Check for Head role
        head = instance.heads.first()
        if head:
            data['head_info'] = {
                "id": head.id,
                "discipline": head.discipline.name,
                # Add any other fields you want
            }
            return data

        # Check for DSA role
        dsa = instance.dsa.first()
        if dsa:
            data['dsa_info'] = {
                "id": dsa.id
            }
            return data

        # Check for Provost role
        provost = instance.provosts.first()
        if provost:
            data['provost_info'] = {
                "id": provost.id
            }
            return data

        # No role found
        return data

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'