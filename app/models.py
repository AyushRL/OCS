from django.db import models

# Create your models here.
class myuser(models.Model):
    id = models.CharField(max_length=50 , primary_key = True)
    hash = models.CharField(max_length = 200)
    is_admin = models.BooleanField()