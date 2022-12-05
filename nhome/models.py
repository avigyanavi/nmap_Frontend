from django.db import models

class nhome(models.Model):
    username = models.CharField(max_length=50)
    pass1 = models.CharField(max_length=250)
