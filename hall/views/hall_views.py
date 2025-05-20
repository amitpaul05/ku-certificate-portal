from django.db.models import Prefetch
from rest_framework.generics import ListAPIView, RetrieveAPIView
from hall.serializers.hall_serializers import HallSerializer
from hall.models import Hall, Provost



class HallListAPIView(ListAPIView):
    serializer_class = HallSerializer

    def get_queryset(self):
        return Hall.objects.prefetch_related(
            Prefetch('provosts', queryset=Provost.objects.current())
        )


class HallDetailAPIView(RetrieveAPIView):
    serializer_class = HallSerializer
    queryset = Hall.objects.prefetch_related(
        Prefetch('provosts', queryset=Provost.objects.current())
    )
    lookup_field = 'id'