# Generated by Django 5.0.4 on 2024-04-26 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_event_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='tickets_sold',
            field=models.IntegerField(default=0),
        ),
    ]
