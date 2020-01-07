# Generated by Django 3.0.1 on 2020-01-07 10:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('importance', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('field', models.CharField(default='', max_length=50)),
                ('commentary', models.CharField(default='', max_length=100)),
                ('comprehense', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
            ],
        ),
    ]