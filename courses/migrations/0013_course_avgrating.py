# Generated by Django 3.0.8 on 2020-08-11 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_auto_20200811_0315'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='avgRating',
            field=models.FloatField(default=0.0),
        ),
    ]