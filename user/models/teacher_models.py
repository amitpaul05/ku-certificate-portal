from django.db import models
from discipline.models.discipline_models import Discipline

from acs import settings


class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='teachers')
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, related_name='teachers')


    class Meta:
        db_table = 'teacher'
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

    def __str__(self):
        return f'{self.user.get_full_name()}'
