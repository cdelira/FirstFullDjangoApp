from django.db import models

class Realtors(models.Model):
    name=models.CharField(max_length=200)
