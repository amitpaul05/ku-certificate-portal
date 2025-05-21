from django.contrib.auth import get_user_model
from rest_framework.generics import GenericAPIView, get_object_or_404, UpdateAPIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from user.serializers.user_serializer import UserSerializer, UserDetailsSerializer
from user.serializers.update_user_serializers import UpdateUserSerializer, UpdatePasswordSerializer
from user.serializers.user_serializer import CustomTokenObtainPairSerializer
User = get_user_model()


class UserAPIView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={
            'request': request
        })
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(data={
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class UserDetailsAPIView(GenericAPIView):
    serializer_class = UserDetailsSerializer
    queryset = User.objects.all()
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        queryset = self.get_object()
        serializer = self.serializer_class(queryset, context={
            'request': request
        })
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserUpdateProfileAPIView(UpdateAPIView):
    lookup_field = 'id'
    queryset = User.objects.all()
    # permission_classes = (IsAuthenticated, IsOwnProfile)
    serializer_class = UpdateUserSerializer


class UserPasswordChangeAPIView(UpdateAPIView):
    lookup_field = 'id'
    serializer_class = UpdatePasswordSerializer
    # permission_classes = [IsAuthenticated, IsOwnProfile]
    queryset = User.objects.all()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, context={'request': request})

        if serializer.is_valid(raise_exception=True):
            instance.set_password(serializer.validated_data['new_password'])
            instance.save()
            return Response({"detail": "Password updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user_data = response.data.pop('user', None)
        if user_data:
            response.data.update(user_data.id)
        return response