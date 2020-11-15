from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres import fields
# Create your models here.


class Host(models.Model):
    hostname = models.CharField(max_length=100)
    api_user = models.OneToOneField(to=User, on_delete=models.CASCADE)


class Data(models.Model):
    host = models.ForeignKey(to=Host, on_delete=models.CASCADE)
    cpu = models.FloatField(blank=True, null=True)
    processes = fields.ArrayField(base_field=models.JSONField(), blank=True, null=True)
    memory = models.JSONField(blank=True, null=True)
    disk = models.JSONField(blank=True, null=True)
    date = models.DateTimeField()
