from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class SessionYearModel(models.Model):
   session_start_year = models.DateField()
   session_end_year = models.DateField()

   def __str__(self):
       return f"{self.session_start_year} - {self.session_end_year}"


class Course(models.Model):
   name = models.CharField(max_length=255, verbose_name='Course Name', )
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   def __str__(self):
       return self.name

from students.models import Profile as StudentProfile
from teachers.models import Profile as TeacherProfile
Students = StudentProfile
Teachers = TeacherProfile


class Subject(models.Model):
   name = models.CharField(max_length=255, verbose_name="Subject Name")
   course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
   teacher_id = models.ForeignKey(User, on_delete=models.CASCADE)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   def __str__(self):
      return self.name


class Attendance(models.Model):
   subject_id = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
   attendance_date = models.DateField(auto_now_add=True)
   session_year_id = models.ForeignKey(SessionYearModel, on_delete=models.CASCADE)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   def __str__(self):
      return f"Attendance for {self.subject_id} - Year: {self.session_year_id}"


class AttendanceReport(models.Model):
   status = models.BooleanField(default=False)
   student_id = models.ForeignKey(Students, on_delete=models.DO_NOTHING)
   attendance_id = models.ForeignKey(Attendance, on_delete=models.CASCADE)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now_add=True)


class LeaveReportStudent(models.Model):
   student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
   leave_date = models.CharField(max_length=255)
   leave_message = models.TextField()
   leave_status = models.IntegerField(default=0)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now_add=True)



class LeaveReportTeacher(models.Model):
   teacher_id = models.ForeignKey(Teachers, on_delete=models.CASCADE)
   leave_date = models.CharField(max_length=255)
   leave_message = models.TextField()
   leave_status = models.BooleanField(default=False)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)


class FeedbackStudent(models.Model):
   student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
   feedback = models.TextField()
   feedback_reply = models.TextField()
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)


class FeedbackTeacher(models.Model):
   teacher_id = models.ForeignKey(Teachers, on_delete=models.CASCADE)
   feedback = models.CharField(max_length=255)
   feedback_reply = models.TextField()
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)


class NotificationStudent(models.Model):
   student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
   message = models.TextField()
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now_add=True)


class NotificationTeacher(models.Model):
   staff_id = models.ForeignKey(Teachers, on_delete=models.CASCADE)
   message = models.TextField()
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)


class StudentResult(models.Model):
   student_id = models.ForeignKey(Students, on_delete=models.DO_NOTHING)
   subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
   subject_exam_marks = models.FloatField(default=0)
   subject_assignment_marks = models.FloatField(default=0)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now_add=True)

