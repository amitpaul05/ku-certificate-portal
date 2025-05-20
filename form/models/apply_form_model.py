from django.db import models

from hall.models import Hall
from user.models import Student, Librarian
from discipline.models import Discipline, Head
from dsa.models import Dsa



class ApplyForm(models.Model):
    DEGREE_CHOICES = [
        ('bachelor', 'Bachelor'),
        ('masters', 'Masters'),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='apply_forms')
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, related_name='apply_forms')
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, related_name='apply_forms')
    degree = models.CharField(max_length=10, choices=DEGREE_CHOICES, default='bachelor')
    is_head_approved = models.BooleanField(default=False)
    head_approved_by = models.ForeignKey(
        Head, on_delete=models.CASCADE, related_name='apply_forms',
        null=True, blank=True
    )
    is_librarian_approved = models.BooleanField(default=False)
    librarian_approved_by = models.ForeignKey(
        Librarian, on_delete=models.CASCADE, related_name='apply_forms',
        null=True, blank=True
    )
    is_dsa_approved = models.BooleanField(default=False)
    dsa_approved_by = models.ForeignKey(
        Dsa, on_delete=models.CASCADE, related_name='apply_forms',
        null=True, blank=True
    )
    is_controller_approved = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    total_credit = models.DecimalField(max_digits=10, decimal_places=2)
    earned_credit = models.DecimalField(max_digits=10, decimal_places=2)
    cgpa = models.DecimalField(max_digits=10, decimal_places=2)
    date_of_last_exam = models.DateField()


    class Meta:
        db_table = "apply_form"
        verbose_name = "Apply Form"
        verbose_name_plural = "Apply Forms"

    def __str__(self):
        return f"{self.student} - {self.discipline} - {self.degree}"



