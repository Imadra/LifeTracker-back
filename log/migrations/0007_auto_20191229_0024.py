# Generated by Django 3.0.1 on 2019-12-28 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0006_auto_20191229_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='log',
            name='time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]