# Generated by Django 3.2 on 2021-06-02 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_checkin_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timecard',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='timeCards', to='app.employee'),
        ),
    ]