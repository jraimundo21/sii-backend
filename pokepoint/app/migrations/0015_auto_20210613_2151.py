# Generated by Django 3.2 on 2021-06-13 20:51

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20210613_0333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='user',
        ),
        migrations.AddField(
            model_name='employee',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(1900, 1, 1, 0, 0), verbose_name='last login'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='last_login',
            field=models.DateTimeField(auto_now=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='employee',
            name='password',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='employee',
            name='username',
            field=models.CharField(default=True, max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=60, unique=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='nif',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='worksAtCompany',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.company'),
        ),
        migrations.DeleteModel(
            name='Manager',
        ),
    ]
