from django.db import models

class Details(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    hobby = models.CharField(max_length=100)

    def __str__(self):
        return self.name
