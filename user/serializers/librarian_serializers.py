from rest_framework import serializers
from user.models import Librarian

class LibrarianSerializer(serializers.ModelSerializer):

    class Meta:
        model = Librarian
        fields = '__all__'