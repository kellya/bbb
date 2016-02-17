from django.db import models

# Create your models here.

class Temp(models.Model):
	timestamp = models.DateTimeField()
	reading  = models.IntegerField()
