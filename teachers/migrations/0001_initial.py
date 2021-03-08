# Generated by Django 3.1.4 on 2021-01-02 14:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import teachers.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to=teachers.models.upload_location)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=25, null=True)),
                ('skills', models.TextField(blank=True, max_length=255, null=True)),
                ('about', models.TextField(blank=True, max_length=255, null=True)),
                ('eductation', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
