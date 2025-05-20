from rest_framework import serializers

from hall.models import Hall
from hall.serializers.provost_serializers import ProvostSerializer


class HallSerializer(serializers.ModelSerializer):
    current_provost = serializers.SerializerMethodField()

    class Meta:
        model = Hall
        fields = '__all__'

    def get_current_provost(self, obj):
        provost = obj.provosts.current().first()  # Use the custom manager!
        if provost:
            return ProvostSerializer(provost).data
        return None