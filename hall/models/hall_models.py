from django.db import models



class Hall(models.Model):
    name = models.CharField(max_length=100)