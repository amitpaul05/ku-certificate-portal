from django.utils import timezone



class DateRangeStatusMixin:
    @property
    def is_current(self):
        today = timezone.now().date()
        return self.start_date <= today <= self.end_date
