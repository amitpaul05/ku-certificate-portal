from django.db import models

from user.models import Teacher


class Dsa(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="dsa")
    start_date = models.DateField()
    end_date = models.DateField()


    class Meta:
        db_table = "dsa"
        verbose_name_plural = "DSAs"
        verbose_name = "DSA"

    def __str__(self):
        return self.teacher.user.get_full_name()