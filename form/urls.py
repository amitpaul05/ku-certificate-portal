from django.urls import path
from form.views.apply_form_views import ApplyFormListCreateView


urlpatterns = [
    path("", ApplyFormListCreateView.as_view(), name='form_list_create'),
    # path("/<str:id>", HallDetailAPIView.as_view(), name='hall_details'),
]