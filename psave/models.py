from django.db import models
from django.contrib.postgres import fields
# Create your models here.


class Host(models.Model):
    hostname = models.CharField(max_length=100)


class Data(models.Model):
    host = models.ForeignKey(to=Host, on_delete=models.CASCADE)
    # date = autofilled date field or date from form request body?
    cpu = models.FloatField()
    processes = fields.ArrayField(base_field=fields.JSONField)
    memory = fields.JSONField()
    disk = fields.JSONField()
