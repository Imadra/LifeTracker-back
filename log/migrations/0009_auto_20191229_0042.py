# Generated by Django 3.0.1 on 2019-12-28 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0008_auto_20191229_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='category',
            field=models.CharField(choices=[('DS', 'DISCOVERY'), ('DP', 'DEPRESSIVE'), ('HP', 'HAPPY'), ('O', 'OTHER')], default='O', max_length=2),
        ),
    ]