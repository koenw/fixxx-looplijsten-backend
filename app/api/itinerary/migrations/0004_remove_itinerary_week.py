# Generated by Django 2.1.9 on 2019-11-04 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itinerary', '0003_auto_20191104_1447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itinerary',
            name='week',
        ),
    ]
