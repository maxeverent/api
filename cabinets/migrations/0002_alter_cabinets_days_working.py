# Generated by Django 4.1.2 on 2022-11-04 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cabinets',
            name='days_working',
            field=models.CharField(max_length=50),
        ),
    ]