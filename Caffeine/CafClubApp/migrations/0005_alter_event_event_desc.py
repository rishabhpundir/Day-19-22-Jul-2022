# Generated by Django 3.2.4 on 2022-07-22 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CafClubApp', '0004_alter_event_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_desc',
            field=models.TextField(blank=True, verbose_name='Event Description'),
        ),
    ]
