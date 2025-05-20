from rest_framework.generics import ListCreateAPIView

from form.models import ApplyForm
from form.serializers.apply_form_serializers import ApplyFormSerializer



class ApplyFormListCreateView(ListCreateAPIView):
    queryset = ApplyForm.objects.all()
    serializer_class = ApplyFormSerializer