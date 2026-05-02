"""
URL configuration for AttendanceProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainapp import views as main_views
from teacherapp import views as teacher_views
from studentapp import views as student_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Main Urls
    path('', main_views.home, name = 'home'),
    path('contactus', main_views.contactUs, name = 'contactus'),
    path('aboutus', main_views.aboutUs, name = 'aboutus'),

    # Student Urls
    path('student-login', student_views.studentLogin, name = 'student_login'),
    path('student-forgot-password', student_views.studentForgotPwd, name = 'student_forgot_password'),
    path('student-dashbord', student_views.studentDashboard, name = 'student_dashboard'),
    path('student-profile', student_views.studentProfile, name = 'student_profile'),
    path('student-attendance-details', student_views.studentAttendaceDetails, name = 'student_attendance_details'),
    path('student-record-attendance', student_views.studentRecordAttendace, name = 'student_record_attendance'),
    path('student-logout', student_views.studentLogout, name = 'student_logout'),

    # Teacher Urls
    path('teacher-login', teacher_views.teacherLogin, name = 'teacher_login'),
    path('teacher-dashboard', teacher_views.teacherDashboard, name = 'teacher_dashboard'),
    path('teacher-forgot-password', teacher_views.teacherForgotPwd, name = 'teacher_forgot_password'),
    path('teacher-add-class-details', teacher_views.teacherAddClassDetails, name = 'teacher_add_class_details'),
    path('teacher-add-class-location', teacher_views.teacherAddClassLocation, name = 'teacher_add_class_location'),
    path('teacher-add-class-location-form/<int:id>', teacher_views.teacherAddLocationForm, name = 'teacher_add_class_location_form'),
    path('teacher-add_student', teacher_views.teacherAddStudent, name = 'teacher_add_student'),
    path('teacher-manage-student', teacher_views.teacherManageStudent, name = 'teacher_manage_student'),
    path('teacher-all-students', teacher_views.allStudents, name = 'teacher_all_students'),
    path('teacher-active-students', teacher_views.teacherActiveStudents, name = 'teacher_active_students'),
    path('strt-qr-code/<int:id>', teacher_views.startQRBtn, name = 'qr_code'),
    path('end-qr-code/<int:id>', teacher_views.endQRBtn, name = 'end_qr_code'),
    path('delete-class/<int:id>', teacher_views.deleteBtn, name = 'delete_class'),
    path('teacher-attendance-details', teacher_views.teacherAttendanceDetails, name = 'teacher_attendance_details'),
    path('teacher-graph-details/<int:id>', teacher_views.teacherGraph, name = 'teacher_graph'),
    path('teacher-edit-student/<int:id>', teacher_views.teacherEditStudent, name = 'teacher_edit_student'),
    # path('teacher-graph-analysis', teacher_views.teacherGraphAnalysis, name = 'teacher_graph_analysis'),
    path('teacher-reocrd-attendance', teacher_views.teacherRecordAttednace, name = 'teacher_record_attendance'),
    path('teacher-statistics-analysis', teacher_views.teacherStatisticsAnalysis, name = 'teacher_statistics_analysis'),
    path('teacher-student-statistic/<int:id>', teacher_views.teacherStudentStatistic, name = 'teacher_student_statistic'),
    path('teacher-load-balancing', teacher_views.teacherLoadBalancing, name = 'teacher_load_balancing'),
    path('teacher-logout', teacher_views.teacherLogout, name = 'teacher_logout'),
    path('delte-student/<int:id>', teacher_views.deleteStudent, name = 'delete_student'),
    path('change-student-status/<int:id>', teacher_views.changeStudentStatus, name = 'change_student_status'),
    path('add-class-location/<int:id>', teacher_views.location_btn, name = 'add_class_location'),
    path('edit-class-location/<int:id>', teacher_views.teacherEditLocation, name = 'teacher_edit_class_location'),
    # path('quick-view', teacher_views.quick_view, name = 'quick-view'),
    # path('quick-view1', teacher_views.quick_view1, name = 'quick-view1'),
    path('student-MyAttendance', student_views.studentMyAttendance, name = 'student_myattendance'),

    # path('quick-view-graph', teacher_views.quick_view_graph, name = 'quick-view-graph'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
