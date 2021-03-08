from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db import models
User = get_user_model()
from helpers.models import SessionYearModel, Course




def upload_location(instance, filename, *args, **kwargs):
   file_path = 'profile/students/{user_id}/{filename}'.format(user_id=str(instance.user.id), filename=filename)
   return file_path

class Profile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
   image = models.ImageField(default='', blank=True, null=True, upload_to=upload_location)
   address = models.CharField(max_length=255, null=True, blank=True)
   phone_number = models.CharField(max_length=25, null=True, blank=True)
   skills = models.TextField(max_length=255, null=True, blank=True)
   about = models.TextField(max_length=255, null=True, blank=True)
   gender = models.CharField(max_length=255, default='Not set')
   reg_number = models.CharField(max_length=255, null=True, blank=True)
   date_of_birth = models.DateField(auto_now_add=False, null=True, blank=True)
   fcm_token = models.TextField(default='')
   course_id = models.ForeignKey(Course, on_delete=models.DO_NOTHING, null=True, blank=True) #when ready, use default instead
   session_year_id = models.ForeignKey(SessionYearModel, on_delete=models.CASCADE, null=True, blank=True) #when ready, use default instead

   def __str__(self):
      return f"{self.user.username}'s Profile"


def user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_student:
          Profile.objects.create(user=instance)
 
post_save.connect(user_profile, sender=User)

@receiver(post_delete, sender=Profile)
def delete_image(sender, instance, *args, **kwargs):
    instance.image.delete(False)


