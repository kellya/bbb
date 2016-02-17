from django.db import models

class State(models.Model):
	port = models.CharField(max_length=5)
	poweron = models.BooleanField()
