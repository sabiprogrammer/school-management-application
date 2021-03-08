from django.urls import path
 
from .views import add_teacher, add_course, add_student, add_subject

app_name = 'superadmin'

urlpatterns = [
    path('teacher', add_teacher, name='add_teacher'),
    path('course', add_course, name='add_course'),
    path('student', add_student, name='add_student'),
    path('subject', add_subject, name='add_subject'),
]
