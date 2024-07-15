from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name