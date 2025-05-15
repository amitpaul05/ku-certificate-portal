from django.db import models

from hall.models.hall_models import Hall
from user.models import Teacher
from django.utils import timezone
from utils.managers.date_range_manager import DateRangeManager
from utils.mixins.date_range_mixins import DateRangeStatusMixin


class Provost(DateRangeStatusMixin, models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='provosts')
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, related_name='provosts')
    start_date = models.DateField()
    end_date = models.DateField()

    objects = DateRangeManager()


    def __str__(self):
        return f"{self.teacher} ({self.start_date} to {self.end_date})"

