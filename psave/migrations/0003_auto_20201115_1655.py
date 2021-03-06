# Generated by Django 3.1.3 on 2020-11-15 16:55

import django.contrib.postgres.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('psave', '0002_host_api_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='data',
            name='cpu',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='disk',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='memory',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='processes',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.JSONField(), blank=True, null=True, size=None),
        ),
    ]
