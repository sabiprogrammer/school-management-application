from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

from helpers.models import Course, SessionYearModel, Subject
from students.models import Profile as StudentProfile


class AddCourseForm(forms.ModelForm):
   class Meta:
      model = Course
      fields = ['name']
      widgets = {
         'name': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Course Name...',
         })
      }


class AddStudentForm(forms.ModelForm):
   password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))
   password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password Again'}))

   course_list = []
   courses = Course.objects.all()
   for course in courses:
      small_course = (course.id, course.name)
      course_list.append(small_course)

   session_list = []
   sessions = SessionYearModel.objects.all()
   for session in sessions:
      small_session = (session.id, str(session.session_start_year) + '  <--->  ' + str(session.session_end_year))
      session_list.append(small_session)

   gender_choice = (
      ("Male", "Male"),
      ("Female", "Female")
   )

   course = forms.ChoiceField(label="Course Name", choices=course_list, widget=forms.Select(attrs={"class": "form-control"}))
   gender = forms.ChoiceField(label="Gender", choices=gender_choice, widget=forms.Select(attrs={"class": "form-control"}))
   session_year_id = forms.ChoiceField(label="Session Year", choices=session_list, widget=forms.Select(attrs={"class": "form-control"}))

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
      user = super(AddStudentForm, self).save(commit=False)
      user.set_password(self.cleaned_data['password1'])

      if commit:
         user.save()
      return user
   



class AddSubjectForm(forms.ModelForm):
   class Meta:
      model = Subject
      fields = ['name']
      widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter subject name',
            })
      }

   course = forms.ModelChoiceField(queryset=Course.objects.all(), label="Course Name", widget=forms.Select(attrs={"class": "form-control"}))
   teacher_id = forms.ModelChoiceField(queryset=User.objects.filter(is_teacher=True), label="Teacher:", widget=forms.Select(attrs={"class": "form-control"}))

