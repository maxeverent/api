# Generated by Django 4.1.2 on 2022-11-05 20:10

import cabinets.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cabinets', '0002_alter_cabinets_days_working'),
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='cabinet_id',
            field=models.ForeignKey(default=cabinets.models.Cabinets.number, null=True, on_delete=django.db.models.deletion.PROTECT, to='cabinets.cabinets'),
        ),
    ]
