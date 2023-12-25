from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Musician(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    instrument_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.username} - {self.instrument_type}"