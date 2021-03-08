from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()


class UserRegisterForm(forms.ModelForm):
   password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))
   password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password Again'}))

   class Meta:
      model = User
      fields = ['username', 'email','first_name', 'last_name', 'other_name', 'password1', 'password2']
      widgets = {
         'username': forms.TextInput(attrs={
               'class': 'form-control',
               'placeholder': 'Enter Username',
         }),
         'email': forms.EmailInput(attrs={
               'class': 'form-control disabled',
               'placeholder': 'Enter Email',
         }),
         'first_name': forms.TextInput(attrs={
               'class': 'form-control',
               'placeholder': 'Enter First Name',
         }),
         'last_name': forms.TextInput(attrs={
               'class': 'form-control',
               'placeholder': 'Enter Last Name',
         }),
         'other_name': forms.TextInput(attrs={
               'class': 'form-control',
               'placeholder': 'Enter Other Names...',
         }),
      }


   def clean_email(self):
      email = self.cleaned_data.get('email').lower()
      qs = User.objects.filter(email=email)
      if qs.exists():
         raise forms.ValidationError("Email Address already taken!")
      return email
   
   def clean_username(self):
      username = self.cleaned_data.get('username').lower()
      qs = User.objects.filter(username=username)
      if qs.exists():
         raise forms.ValidationError("Username already taken!")
      return username
   
   def clean_password2(self):
      password1 = self.cleaned_data.get('password1')
      password2 = self.cleaned_data.get('password2')

      if password1 and password2 and password1 != password2:
         raise forms.ValidationError("Password fields do not match. Recheck...")
      return password2
   
   def save(self, commit=True):
      user = super(UserRegisterForm, self).save(commit=False)
      user.set_password(self.cleaned_data['password1'])

      if commit:
         user.save()
      return user
   

class LoginForm(forms.Form):
   email = forms.EmailField(label='Email Address')
   password = forms.CharField(widget=forms.PasswordInput, label='Password')


# FORMS FOR CREATING AND UPDATING USERS VIA ADMIN PANEL
class UserAdminCreationForm(forms.ModelForm):
   password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
   password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

   class Meta:
      model = User
      fields = ['username', 'email']
   
   def clean_password2(self):
      password1 = self.cleaned_data.get('password1')
      password2 = self.cleaned_data.get('password2')

      if password1 and password2 and password1 != password2:
         raise forms.ValidationError("Password fields do not match. Recheck...")
      return password2
   
   def save(self, commit=True):
      user = super(UserAdminCreationForm, self).save(commit=False)
      user.set_password(self.cleaned_data['password1'])

      if commit:
         user.save()
      return user


class UserAdminUpdateForm(forms.ModelForm):
   password = ReadOnlyPasswordHashField()

   class Meta:
      model = User
      fields = ['username', 'email', 'password', 'is_active', 'is_admin']

   def clean_password(self):
      return self.initial['password']

