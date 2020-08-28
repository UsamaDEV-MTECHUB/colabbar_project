from django.db import models
from passlib.hash import pbkdf2_sha256


# Create your models here.
class userData(models.Model) :
    username = models.CharField(max_length=250)
    fullname = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phoneno = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    verify_link = models.TextField(blank=True)
    verify_status = models.BooleanField(null=True, default=False)
    login_first = models.BooleanField(null=True, default=False)



    def __str__(self) :
        return self.username
