# Generated by Django 3.0.7 on 2020-08-07 11:19

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0008_auto_20200116_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='habit_list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default='', max_length=50), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='person',
            name='strength_list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default='', max_length=50), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='person',
            name='weakness_list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default='', max_length=50), blank=True, default=list, size=None),
        ),
    ]
