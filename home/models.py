from django.db import models
from django.core.validators import MinValueValidator
import random

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Course(models.Model):
    id = models.IntegerField(
        primary_key=True,
        unique=True,
        validators=[MinValueValidator(100000)],
        editable=False
    )
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    create = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    TYPE = [
        ("OF", "Offline"),
        ("ON", "Online"),
        ("AL", "Offline + Online"),
    ]
    type = models.CharField(max_length=2, default="ON", choices=TYPE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = random.randint(100000, 999999)
        super().save(*args, **kwargs)

    