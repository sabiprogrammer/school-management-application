from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

User = get_user_model()

from accounts.forms import UserRegisterForm
from teachers.models import Profile as TeacherProfile
from students.models import Profile as StudentProfile

from .forms import AddCourseForm, AddStudentForm, AddSubjectForm

# def superadmin_home(request):
#    print('USER:', request.user)
#    return HttpResponse("You are now in the superadmin home page")

def add_teacher(request):
   form = UserRegisterForm(request.POST or None)
   if request.method == 'POST':
      print('yyyes')
      if form.is_valid():
         user = form.save(commit=False)
         data = form.cleaned_data

         user.first_name = data.get('first_name')
         user.last_name = data.get('last_name')
         user.other_name = data.get('other_name')
         user.is_teacher = True
         
         user.save()

         # user_profile = TeacherProfile.objects.get(user=user)
         # user_profile.address = 'my address here'
         # user_profile.save()
         full_name = f"{data.get('first_name')} {data.get('last_name')}"

         messages.success(request, f'Teacher "{full_name}" successfully registered.')
         return redirect('helpers:index_page')

   return render(request, 'superadmin/add_teacher.html', context={'form': form})


def add_course(request):
   form = AddCourseForm(request.POST or None)
   if request.method == 'POST':
      if form.is_valid():
         form.save()
         messages.success(request, f'Course successfully created.')
         return redirect('helpers:index_page')
   return render(request, 'add_course.html', context={'form': form})


def add_student(request):
   form = AddStudentForm(request.POST or None)
   from helpers.models import Course, SessionYearModel
   if request.method == 'POST':
      if form.is_valid():
         user = form.save(commit=False)
         data = form.cleaned_data

         user.first_name = data.get('first_name')
         user.last_name = data.get('last_name')
         user.other_name = data.get('other_name')
         user.is_student = True

         user.save()

         course_obj = Course.objects.get(id=data.get('course'))
         student_session = SessionYearModel.objects.get(id=data.get('session_year_id'))

         user_profile = StudentProfile.objects.get(user=user)
         user_profile.gender = form.cleaned_data["gender"]
         user_profile.session_year_id = student_session
         user_profile.course_id = course_obj
         
         user_profile.save()

         messages.success(request, 'Student "' + data.get('first_name') + ' ' + data.get('last_name') + '" added successfully')
         return redirect('helpers:index_page')
   return render(request, 'superadmin/add_student.html', context={'form': form})


def add_subject(request):
   form = AddSubjectForm(request.POST or None)
   from helpers.models import Course, SessionYearModel
   if request.method == 'POST':
      if form.is_valid():
         subject = form.save(commit=False)
         data = form.cleaned_data
         
         subject.course_id = data.get('course')
         subject.teacher_id = data.get('teacher_id')
         subject.save()

         messages.success(request, f'Subject "{subject.name}" added successfully')
         return redirect('helpers:index_page')
   return render(request, 'superadmin/add_subject.html', context={'form': form})


