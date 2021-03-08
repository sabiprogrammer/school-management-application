from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, post_delete
# from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db import models

User = get_user_model()

def upload_location(instance, filename, *args, **kwargs):
   file_path = 'profile/superadmin/{user_id}/{filename}'.format(user_id=str(instance.user.id), filename=filename)
   return file_path

class Profile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='superadmin_profile')
   image = models.ImageField(default='', blank=True, null=True, upload_to=upload_location)
   address = models.CharField(max_length=255, null=True, blank=True)
   phone_number = models.CharField(max_length=25, null=True, blank=True)
   skills = models.TextField(max_length=255, null=True, blank=True)
   about = models.TextField(max_length=255, null=True, blank=True)
   eductation = models.CharField(max_length=255, null=True, blank=True)

   def __str__(self):
      return f"{self.user.username}'s Profile"


def user_profile(sender, instance, created, **kwargs):
    if created:
       if instance.is_superadmin or instance.is_superuser:
          Profile.objects.create(user=instance)
post_save.connect(user_profile, sender=User)

@receiver(post_delete, sender=Profile)
def delete_image(sender, instance, *args, **kwargs):
    instance.image.delete(False)


