# Generated by Django 3.1.4 on 2021-01-03 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_profile_fcm_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(default='Not set', max_length=255),
        ),
    ]
