# Generated by Django 3.0.1 on 2020-01-15 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0011_auto_20200104_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='text',
            field=models.TextField(default='No text', max_length=2500),
        ),
    ]