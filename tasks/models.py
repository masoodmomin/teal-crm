from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200, null=True)
    desc = models.CharField(max_length=300, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)