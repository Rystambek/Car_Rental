from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=80)
    url = models.URLField(unique=True)
    description = models.TextField(default="",blank=True)
    price = models.FloatField()
    color = models.CharField(max_length=80)
    model = models.CharField(max_length=80)
    years = models.IntegerField()
    motors = models.CharField(max_length=80)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)