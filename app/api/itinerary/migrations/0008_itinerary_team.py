# Generated by Django 2.1.11 on 2019-11-11 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_team'),
        ('itinerary', '0007_auto_20191111_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='itinerary',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Team'),
        ),
    ]
