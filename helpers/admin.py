from django.contrib import admin

from .models import (
   Course, SessionYearModel, Subject, Attendance, AttendanceReport, FeedbackStudent, FeedbackTeacher, LeaveReportStudent,
   LeaveReportTeacher, NotificationStudent, NotificationTeacher, 
   )

admin.site.register(Course)
admin.site.register(SessionYearModel)
admin.site.register(Subject)
admin.site.register(Attendance)
admin.site.register(AttendanceReport)
admin.site.register(FeedbackStudent)
admin.site.register(FeedbackTeacher)
admin.site.register(LeaveReportStudent)
admin.site.register(LeaveReportTeacher)
admin.site.register(NotificationStudent)
admin.site.register(NotificationTeacher)
