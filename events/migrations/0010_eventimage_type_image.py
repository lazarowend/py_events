# Generated by Django 5.0.4 on 2024-12-12 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_tickettype_remove_event_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventimage',
            name='type_image',
            field=models.CharField(choices=[('Principal', 'Principal'), ('Extra', 'Extra')], default=1, max_length=50),
            preserve_default=False,
        ),
    ]
