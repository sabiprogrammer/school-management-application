# Generated by Django 3.1.4 on 2021-01-02 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fcm_token',
            field=models.TextField(default=''),
        ),
    ]
