# Generated by Django 3.0.1 on 2020-01-18 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycalendar', '0006_auto_20200118_2146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dayinfo',
            name='date',
        ),
        migrations.AddField(
            model_name='dayinfo',
            name='day',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dayinfo',
            name='month',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dayinfo',
            name='year',
            field=models.IntegerField(default=0),
        ),
    ]
