# Generated by Django 5.0.4 on 2024-12-18 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adresses', '0004_remove_address_place_name_remove_address_public_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='name',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
