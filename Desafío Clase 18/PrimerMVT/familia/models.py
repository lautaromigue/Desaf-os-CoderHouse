from django.db import models

class Familiar(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    birth= models.DateField(null=True, blank=True)
