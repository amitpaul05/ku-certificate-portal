from django.urls import path
from form.views.apply_form_views import ApplyFormListCreateView, HeadFormRetrieveUpdateDestroyView, DsaFormRetrieveUpdateDestroyView, LibrarianFormRetrieveUpdateDestroyView

urlpatterns = [
    path("", ApplyFormListCreateView.as_view(), name='form_list_create'),
    path("/head/<str:id>", HeadFormRetrieveUpdateDestroyView.as_view(), name='form_update_head'),
    path("/dsa/<str:id>", DsaFormRetrieveUpdateDestroyView.as_view(), name='form_update_dsa'),
    path("/librarian/<str:id>", LibrarianFormRetrieveUpdateDestroyView.as_view(), name='form_update_librarian'),
    # path("/<str:id>", HallDetailAPIView.as_view(), name='hall_details'),
]