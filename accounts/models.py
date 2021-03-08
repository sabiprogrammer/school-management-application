from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.db import models


class UserManager(BaseUserManager):
   def create_user(self, email, username, first_name=None, last_name=None, other_name=None, password=None, is_admin=False, is_staff=False, is_superuser=False):
      if not email:
         raise ValueError("Please provide a valid email address.")

      if not password:
         raise ValueError("Please provide a reasonalbe and secured password.")
      if not username:
         raise ValueError("Please provide a unique username for your account.")

      user_obj = self.model(
         email = self.normalize_email(email),
         username = username,
         first_name = first_name,
         last_name = last_name,
         other_name = other_name,
         is_admin = is_admin,
         is_staff = is_staff,
         is_superuser = is_superuser
      )

      user_obj.set_password(password)
      user_obj.save(using=self._db)
      return user_obj
   
   def create_superuser(self, email, username, password):
      user = self.create_user(
         email = self.normalize_email(email),
         password = password,
         username = username,
         is_admin = True,
         is_staff = True,
         is_superuser = True
      )

      user.save(using=self._db)
      return user


class User(AbstractBaseUser):
   first_name = models.CharField(max_length=255, null=True, blank=True)
   last_name = models.CharField(max_length=255, null=True, blank=True)
   other_name = models.CharField(max_length=255, null=True, blank=True)
   username = models.CharField(max_length=255, unique=True)
   email = models.EmailField(max_length=255, unique=True)
   date_created = models.DateTimeField(auto_now_add=True)
   date_updated = models.DateTimeField(auto_now=True)
   is_superuser = models.BooleanField(default=False)
   is_active = models.BooleanField(default=True)
   is_staff = models.BooleanField(default=False)
   is_admin = models.BooleanField(default=False)
   is_superadmin = models.BooleanField(default=False)
   is_student = models.BooleanField(default=False)
   is_teacher = models.BooleanField(default=False)
   
   objects = UserManager()

   # confirmed_email = models.BooleanField(default=False)
   # confirmed_email_date = models.DateTimeField(blank=True, null=True)

   USERNAME_FIELD = 'email'
   REQUIRED_FIELDS = ['username',]

   def __str__(self):
      return f"{self.username}"
   
   def get_full_name(self):
      if self.last_name and self.last_name:
         return f"{self.last_name} {self.first_name} {self.other_name}"
      else:
         return 'Full name not set.'

   
   def has_perm(self, perm, obj=None):
      return self.is_admin
   
   def has_module_perms(self, app_label):
      return True

