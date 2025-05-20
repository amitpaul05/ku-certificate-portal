from django.db import models

from form.models.apply_form_model import ApplyForm
from user.models import Student


class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100)
    form = models.ForeignKey(ApplyForm, on_delete=models.CASCADE, related_name='payments')


    def __str__(self):
        return f"{self.form}"