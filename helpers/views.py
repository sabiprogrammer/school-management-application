from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

User = get_user_model()

from .forms import AddCourseForm


def index_page(request):
   if request.user.is_authenticated:
      if request.user.is_teacher:
         return HttpResponse("You are a teacher!")
      if request.user.is_student:
         return HttpResponse("You are a student!")
      if request.user.is_superadmin or request.user.is_superuser:
         context = {}
         return render(request, 'superadmin/home.html', context)
   else:
      context = {}
      messages.warning(request, "Note that you are not a logged in user, so some activities might be restricted or not function properly.")
      return render(request, 'superadmin/home.html', context)


def all_teachers(request):
   teachers = User.objects.filter(is_teacher=True).order_by('-date_created')
   return render(request, 'superadmin/all_teachers.html', context={'teachers': teachers})


def manage_teachers(request):
   teachers = User.objects.filter(is_teacher=True).order_by('-date_created')
   return render(request, 'superadmin/manage_teachers.html', context={'teachers': teachers})


def teacher_profile(request):
   # teacher = User.objects.get(id=True)
   context={}
   return render(request, 'superadmin/teacher_profile.html')


def all_students(request):
   students = User.objects.filter(is_student=True).order_by('-date_created')
   return render(request, 'superadmin/all_students.html', context={'students': students})


def manage_students(request):
   students = User.objects.filter(is_student=True).order_by('-date_created')
   return render(request, 'superadmin/manage_students.html', context={'students': students})


def student_profile(request):
   # student = User.objects.get(id=True)
   context={}
   return render(request, 'superadmin/student_profile.html')


from helpers.models import Subject, Course
def manage_subjects(request):
   subjects = Subject.objects.all().order_by('-created_at')
   return render(request, 'superadmin/manage_subjects.html', context={'subjects': subjects})


def manage_courses(request):
   courses = Course.objects.all().order_by('-created_at')
   return render(request, 'superadmin/manage_courses.html', context={'courses': courses})

