from django.db import models

from discipline.models import Discipline
from user.models.teacher_models import Teacher

class Head(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="heads")
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, related_name="heads")
    start_date = models.DateField()
    end_date = models.DateField()


    def __str__(self):
        return f"{self.teacher.user.get_full_name()} - {self.discipline.name}"



    class Meta:
        db_table = "head"
        verbose_name = "Head"
        verbose_name_plural = "Heads"