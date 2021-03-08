from django.urls import path
 
from .views import (index_page, all_teachers, manage_teachers, teacher_profile, 
    all_students, manage_students, student_profile, manage_subjects, manage_courses
)

app_name = 'helpers'

urlpatterns = [
    path('', index_page, name='index_page'),
    path('all_teachers', all_teachers, name='all_teachers'),
    path('manage_teachers', manage_teachers, name='manage_teachers'),
    path('teacher_profile', teacher_profile, name='teacher_profile'),

    path('all_students', all_students, name='all_students'),
    path('manage_students', manage_students, name='manage_students'),
    path('student_profile', student_profile, name='student_profile'),

    path('manage_subjects', manage_subjects, name='manage_subjects'),
    path('manage_courses', manage_courses, name='manage_courses'),
    
]
