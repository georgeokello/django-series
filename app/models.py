from django.db import models
from django.db import models

class Data(models.Model):
    username = models.CharField(max_length=120)
    age = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.username} ---- {self.age}"
