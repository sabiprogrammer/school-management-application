from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib import admin

User = get_user_model()

from .forms import UserAdminCreationForm, UserAdminUpdateForm

class UserAdmin(BaseUserAdmin):
   search_fields = ['email', 'username']
   add_form = UserAdminCreationForm
   form = UserAdminUpdateForm

   list_display = ('email', 'username', 'is_admin','is_superadmin', 'is_teacher', 'is_student')
   list_filter = ()
   fieldsets = (
      (None, {'fields': ('email', 'username', 'password', 'last_name', 'first_name')}),
      # ('Personal Info', {'fields': ('username',)}),
      ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_active')}),
   )

   add_fieldsets = (
      (None, {
         'classes': ('wide',),
         'fields': ('email', 'password1', 'password2')
      }),
   )

   ordering = ('email',)
   filter_horizontal = ()

   # class Meta:
   #    model = User
admin.site.register(User, UserAdmin)

# admin.site.unregister(Group)

