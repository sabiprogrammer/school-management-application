from django import forms

from .models import Course


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
      