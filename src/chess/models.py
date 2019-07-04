from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.

class Board(models.Model):
	start_date = models.DateField(auto_now_add=True, auto_now=False)
	board_status = ArrayField(ArrayField(models.IntegerField()))

