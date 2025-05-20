from django.urls import path, include
from hall.views.hall_views import HallListAPIView, HallDetailAPIView


urlpatterns = [
    path("", HallListAPIView.as_view(), name='hall_list'),
    path("/<str:id>", HallDetailAPIView.as_view(), name='hall_details'),
]