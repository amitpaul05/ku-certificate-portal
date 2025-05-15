from django.db import models
from django.utils import timezone

class DateRangeManager(models.Manager):
    def current(self):
        today = timezone.now().date()
        return self.filter(start_date__lte=today, end_date__gte=today)