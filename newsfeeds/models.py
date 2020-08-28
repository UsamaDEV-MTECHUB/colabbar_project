from django.db import models
from passlib.hash import pbkdf2_sha256


# Create your models here.
class feeddata(models.Model) :
    name = models.CharField(max_length=250)

    def __str__(self) :
        return self.name
