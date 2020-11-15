# Generated by Django 3.1.3 on 2020-11-11 22:06

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpu', models.FloatField()),
                ('processes', django.contrib.postgres.fields.ArrayField(base_field=models.JSONField(), size=None)),
                ('memory', models.JSONField()),
                ('disk', models.JSONField()),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psave.host')),
            ],
        ),
    ]