from django.db import models


class Discipline(models.Model):
    name = models.CharField(max_length=100)
    discipline_code = models.CharField(max_length=100)


    class Meta:
        db_table = 'discipline'
        ordering = ['discipline_code']

    def __str__(self):
        return self.name