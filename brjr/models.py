from django.db import models



# makemigrations
# migrate
# in DB Browser, add BDays

class Birthday(models.Model):
	name = models.CharField(max_length=25)
	date = models.DateField(blank=True, null=True)
	greeting = models.CharField(max_length=200)