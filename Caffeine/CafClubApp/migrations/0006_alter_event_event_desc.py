# Generated by Django 3.2.4 on 2022-07-22 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CafClubApp', '0005_alter_event_event_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_desc',
            field=models.CharField(blank=True, max_length=200, verbose_name='Event Description'),
        ),
    ]