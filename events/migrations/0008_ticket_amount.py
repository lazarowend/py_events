# Generated by Django 5.0.4 on 2024-04-26 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_event_tickets_sold'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='amount',
            field=models.IntegerField(default=1),
        ),
    ]
