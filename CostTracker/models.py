from django.db import models


class Cost(models.Model):
    category = models.TextField()
    amount = models.IntegerField()
    date = models.DateField()
    file = models.FileField()
