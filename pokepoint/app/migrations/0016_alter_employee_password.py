# Generated by Django 3.2 on 2021-06-13 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20210613_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
