from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model

from user.serializers.password_reset_serializers import PasswordResetRequestSerializer, PasswordResetConfirmSerializer

User = get_user_model()


class PasswordResetRequestView(APIView):
    """
    API endpoint to request a password reset.

    This view handles user requests for password reset by validating the provided email
    and sending a password reset link to the registered email address.

    Methods:
        - POST: Accepts an email and triggers the password reset process.

    Request Body:
        {
            "email": "user@example.com"
        }

    Responses:
        - 200 OK: Password reset email sent successfully.
        - 400 Bad Request: Invalid input (e.g., missing email or unregistered email).
    """
    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"message": "Password reset email sent."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetConfirmView(APIView):
    """
    API endpoint to confirm and set a new password.

    This view processes the password reset token and allows users to set a new password.

    Methods:
        - POST: Accepts a token and a new password, then updates the user's password.

    Request Body:
        {
            "uid": "user_id",
            "token": "reset-token",
            "new_password": "new_secure_password"
        }

    Responses:
        - 200 OK: Password has been reset successfully.
        - 400 Bad Request: Invalid or expired token, or weak password.
    """
    def post(self, request):
        serializer = PasswordResetConfirmSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"message": "Password has been reset successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
