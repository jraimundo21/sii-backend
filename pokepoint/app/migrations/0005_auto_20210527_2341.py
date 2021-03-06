# Generated by Django 3.2 on 2021-05-27 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_checkout_checkintype'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkin',
            name='timestamp',
            field=models.DateTimeField(default=None, verbose_name='time of checkin'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='checkout',
            name='timestamp',
            field=models.DateTimeField(default=None, verbose_name='time of checkout'),
            preserve_default=False,
        ),
    ]
