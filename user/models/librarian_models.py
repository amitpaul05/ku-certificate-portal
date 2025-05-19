from django.db import models

from user.models import User


class Librarian(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='librarians')
    start_date = models.DateField()
    end_date = models.DateField()


    def __str__(self):
        return str(self.user)
