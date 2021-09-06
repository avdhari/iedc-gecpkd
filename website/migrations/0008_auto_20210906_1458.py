# Generated by Django 3.2.6 on 2021-09-06 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_alter_event_event_is_live'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_hustle_chat',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='yt_link',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
