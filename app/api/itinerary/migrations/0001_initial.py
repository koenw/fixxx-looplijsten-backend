# Generated by Django 2.1.9 on 2019-11-04 13:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('week', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(52), django.core.validators.MinValueValidator(1)])),
                ('plain_text_itinerary', models.TextField(blank=True, max_length=4000)),
            ],
        ),
        migrations.CreateModel(
            name='ItineraryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_id', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('itinerary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itinerary.Itinerary')),
            ],
        ),
    ]
