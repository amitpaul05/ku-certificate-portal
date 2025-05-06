from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)
from user.views.student_views import StudentListView

from user.views.user_api_view import (
    UserAPIView,
    CustomTokenObtainPairView,
    UserDetailsAPIView,
    UserUpdateProfileAPIView,
    UserPasswordChangeAPIView
)

from user.views.password_reset_views import (
    PasswordResetRequestView,
    PasswordResetConfirmView
)

urlpatterns = [
    path('student/', StudentListView.as_view(), name='student-list'),
    path('token/', CustomTokenObtainPairView.as_view(), name=''),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('register/', UserAPIView.as_view(), name='user-registration'),
    path('password-reset/', PasswordResetRequestView.as_view(), name='password_reset_request'),
    path('password-reset-confirm/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('<str:id>/', UserDetailsAPIView.as_view(), name='user-details'),
    path('<str:id>/edit/', UserUpdateProfileAPIView.as_view(), name='update-user-details'),
    path('<str:id>/change-password/', UserPasswordChangeAPIView.as_view(), name='change-user-password'),
]