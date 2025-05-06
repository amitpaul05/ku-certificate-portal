from django.db import models
from django_countries.fields import CountryField
from discipline.models.discipline_models import Discipline

from acs import settings


class Student(models.Model):
    student_id = models.CharField(max_length=20, primary_key=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student')
    nationality = CountryField(blank_label='(select country)', default='BD')
    father_name = models.CharField(max_length=20)
    mother_name = models.CharField(max_length=20)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, related_name='students')


    class Meta:
        db_table = 'student'
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return f'{self.user.get_full_name()}'

