from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Album(models.Model):
    name=models.CharField(max_length=20)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    relase_date=models.DateField()
    rating=models.IntegerField(choices=[(i,i) for i in range(1,6)])

    def __str__(self):
        return self.name


