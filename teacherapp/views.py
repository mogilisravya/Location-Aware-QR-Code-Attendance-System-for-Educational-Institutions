from django.shortcuts import render, redirect
from teacherapp.models import *
from studentapp.models import *
import random
import string
import qrcode
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File
import time
from django.contrib import messages
# from django.http import JsonResponse
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
import qrcode

# Create your views here.

# Teacher Login
def teacherLogin(req):
    teacher_id = 'admin'
    teacher_pwd = 'admin'
    if req.method == 'POST':
        t_id = req.POST.get('teacherId')
        t_pwd = req.POST.get('tPwd')
        if (t_id == teacher_id and t_pwd == teacher_pwd):
            messages.success(req, 'Login Successfull..!')
            return redirect('teacher_dashboard')
        else:
            return redirect('teacher_login')
    return render(req, 'main/main-teacher-login.html')

# Teacher Forgot Password
def teacherForgotPwd(req):
    return render(req, 'main/main-teacher-forgot-password.html')

# Teacher Dashboard
def teacherDashboard(req):
    student_online_count = Student_Details_Model.objects.filter(Student_Online_Status = 'online').count()
    students_count = Student_Details_Model.objects.all().count()
    students_penidng_count = Student_Details_Model.objects.filter(Student_Status = 'pending').count()
    students_rejected_count = Student_Details_Model.objects.filter(Student_Status = 'rejected').count()
    return render(req, 'teacher/index.html', {'i' : student_online_count, 'a':students_count, 'b':students_penidng_count, 'c':students_rejected_count})

# Teacher Add Student
def teacherAddStudent(req):
    if req.method == 'POST' and req.FILES['sProfile']:
        stu_name = req.POST.get('sName')
        stu_age = req.POST.get('sAge')
        stu_email = req.POST.get('sEmail')
        stu_address = req.POST.get('sAddress')
        stu_section = req.POST.get('sSection')
        stu_rollnumber = req.POST.get('sRollNum')
        stu_branch = req.POST.get('sBranch')
        stu_gender = req.POST.get('sGender')
        stu_phnum = req.POST.get('sPhnum')
        stu_profile = req.FILES['sProfile']
        stu_char = string.ascii_letters + string.digits
        stu_pwd = ''.join(random.choices(stu_char, k=4))
        Student_Details_Model.objects.create(Student_Name = stu_name, Student_Age = stu_age, Student_Email = stu_email, Student_Address = stu_address, Student_Section = stu_section, Student_RollNumber = stu_rollnumber, Student_Branch = stu_branch, Student_Gender = stu_gender, Student_Phone_Number = stu_phnum, Student_Profile = stu_profile, Student_Password = stu_pwd)
        mail_message = f'Registration Successfully\n Your Login Password is\n {stu_pwd}'
        print(mail_message)
        send_mail("Student Password", mail_message , settings.EMAIL_HOST_USER, [stu_email])
        messages.success(req, 'Student added Successfully..!')
    return render(req, 'teacher/teacher-add-student.html')

# Teacher Manage Student
def teacherManageStudent(req):
    student = Student_Details_Model.objects.all().order_by("Student_Id")
    paginator = Paginator(student, 5) 
    page_number = req.GET.get('page')
    post = paginator.get_page(page_number)
    return render(req, 'teacher/teacher-manage-student.html', {'student' : post})

# Delete Student
def deleteStudent(req, id):
    a = Student_Details_Model.objects.get(Student_Id = id).delete()
    messages.warning(req, 'Student deleted Successfully..!')
    return redirect('teacher_manage_student')

# Change Student Status
def changeStudentStatus(req, id):
    student_detail  = Student_Details_Model.objects.get(Student_Id = id)
    if (student_detail.Student_Status == 'pending'):
        student_detail.Student_Status = 'accepted'
        student_detail.save()
        messages.info(req, 'Student status was changed to Accepted..!')
    elif (student_detail.Student_Status == 'accepted'):
        student_detail.Student_Status = 'rejected'
        student_detail.save()
        messages.info(req, 'Student status was changed to Rejected..!')
    elif (student_detail.Student_Status == 'rejected'):
        student_detail.Student_Status = 'accepted'
        student_detail.save()
        messages.info(req, 'Student status was changed to Accepted..!')
    else:
        student_detail.Student_Status = 'accepted'
        student_detail.save()
    return redirect('teacher_manage_student')

# All Students
def allStudents(req):
    student = Student_Details_Model.objects.all().order_by("Student_Id")
    paginator = Paginator(student, 5) 
    page_number = req.GET.get('page')
    post = paginator.get_page(page_number)
    return render(req, 'teacher/teacher-all-students.html', {'s' : post})

# Teacher Edit Student
def teacherEditStudent(req, id):
    stu_info = Student_Details_Model.objects.get(Student_Id = id)
    print(stu_info.Student_Name)
    if req.method == 'POST' :
        stu_name = req.POST.get('stName')
        stu_age = req.POST.get('stAge')
        stu_email = req.POST.get('stEmail')
        stu_gender = req.POST.get('stGen')
        # stu_pic = req.POST.get('stPic')
        stu_branch = req.POST.get('stBranch')
        stu_section = req.POST.get('stSection')
        stu_pwd = req.POST.get('stPwd')
        stu_rollnum = req.POST.get('stRollnum')

        if len(req.FILES) != 0:
            stu_pic = req.FILES['stPic']
            stu_info.Student_Name = stu_name
            stu_info.Student_Age = stu_age
            stu_info.Student_Email = stu_email
            stu_info.Student_Gender = stu_gender
            stu_info.Student_Branch = stu_branch
            stu_info.Student_Password = stu_pwd
            stu_info.Student_Profile = stu_pic
            stu_info.Student_Section = stu_section
            # stu_info.Student_RollNumber = stu_rollnum
            stu_info.save()
        else:
            stu_info.Student_Name = stu_name
            stu_info.Student_Email = stu_email
            stu_info.Student_Age = stu_age
            stu_info.Student_Gender = stu_gender
            stu_info.Student_Branch = stu_branch
            stu_info.Student_Password = stu_pwd
            stu_info.Student_Section = stu_section
            stu_info.Student_RollNumber = stu_rollnum
            stu_info.save()
        return redirect('teacher_edit_student', id=id)
    return render(req, 'teacher/teacher-edit-student.html', {'stuinfo' : stu_info})

# Pop up Ajax for Attendance details
# def quick_view(request):
#     # print('function')
#     id = request.GET.get('id')
#     # print(id, 'id')
#     stu_present = Attendance_Details_Model.objects.filter(Cla_Foregin__Class_Id = id, Att_Status = 'present').count()
#     cla_info = Class_Details_Model.objects.get(Class_Id = id)
#     stu_info = Student_Details_Model.objects.filter(Student_Branch = cla_info.Branch_Name, Student_Section = cla_info.Section).count()
#     stu_absent = stu_info - stu_present
#     # print(stu_present, 'a', stu_absent, 'a', stu_info)
#     data = {
#         'total_stu' : stu_info,
#         'present' : stu_present,
#         'absent' : stu_absent,
#     } 
#     # print(data)
#     return JsonResponse(data)

# Pop up Ajax for statistics analysis
# def quick_view1(request):
#     # print('function11')
#     id = request.GET.get('id')
#     # print(id, 'student')
#     stu_info = Student_Details_Model.objects.get(Student_Id = id)
#     cla = Class_Details_Model.objects.filter(Branch_Name = stu_info.Student_Branch, Section = stu_info.Student_Section)
#     # print(cla, 'classes count')
#     atten_count = Attendance_Details_Model.objects.filter(Student_Rollnum = stu_info.Student_RollNumber).count()
#     stu_name = stu_info.Student_Name
#     z = 0
#     for i in cla:
#         z +=  i.Class_Count
#         stu_absent_count =  z - atten_count 
#         # print(z,'class')
#     data = {
#         'count' : z,
#         'atten' : atten_count,
#         'name' : stu_name,
#         'absent' : stu_absent_count,
#         }
#     return JsonResponse(data)

# Pop up Ajax for Graph
# def quick_view_graph(request):
#     print('function12')
#     id = request.GET.get('id')
#     print(id)
#     stu_info = Student_Details_Model.objects.get(Student_Id = id)
#     data = {
        
#         }
#     return JsonResponse(data)

# Active Students Tabel
def teacherActiveStudents(req):
    student_data = Student_Details_Model.objects.filter(Student_Online_Status = 'online').order_by("Student_Id")
    paginator = Paginator(student_data, 5) 
    page_number = req.GET.get('page')
    post = paginator.get_page(page_number)
    return render(req, 'teacher/teacher-active-students.html', {'stud' : post})

# Teacher Add Class Details0
def teacherAddClassDetails(req):
    if req.method == 'POST':
        cla_incha_name = req.POST.get('claInchaName')
        cla_subj_name = req.POST.get('claSubjName')
        cla_branch_name = req.POST.get('claBranch')
        cla_section = req.POST.get('claSection')
        cla_duration = req.POST.get('claDuration')
        cla_sta_time = req.POST.get('claStaTime')
        cla_end_time = req.POST.get('claEndTime')
        print(cla_sta_time)
        try:
            Class_Details_Model.objects.get(Class_Start_Time = cla_sta_time)
            return redirect('teacher_add_class_details')
        except:
            Class_Details_Model.objects.create(Class_Incharge_Name = cla_incha_name, Subject_Name = cla_subj_name, Branch_Name = cla_branch_name, Section = cla_section, Class_Start_Time = cla_sta_time, Class_End_Time = cla_end_time)
            messages.success(req, 'Class was added Successfully..!')
            return redirect('teacher_add_class_details')
    return render(req, 'teacher/teacher-add-class-details.html')

# Add Class Location Button
def location_btn (req, id):
    # class_loca = Class_Details_Model.objects.get(Class_Id = id)
    # if req.method == 'POST':
    #     cla_floor_num = req.POST.get('claFloNum')
    #     cla_room_num = req.POST.get('claRoomNum')
    #     cla_longitude = req.POST.get('claLongit')
    #     cla_latitude = req.POST.get('claLatit')
    #     Class_Details_Model.objects.update(Class_Floor_Number = cla_floor_num, Class_Room_Number = cla_room_num, Class_Latitude = cla_latitude, Class_Longitude = cla_longitude)
    #     return redirect('teacher_add_class_location_form')
    return redirect('teacher_add_class_location_form')
# Teacher Add Class Location
def teacherAddClassLocation(req):
    classes = Class_Details_Model.objects.all().order_by("Class_Id")
    paginator = Paginator(classes, 5) 
    page_number = req.GET.get('page')
    post = paginator.get_page(page_number)
    return render(req, 'teacher/teacher-add-class-location-details.html', {'clas' : post})

# Teacher Add Location Form
def teacherAddLocationForm(req, id):
    class_loca = Class_Details_Model.objects.get(Class_Id = id)
    # print(id)
    if req.method == 'POST':
        cla_floor_num = req.POST.get('claFloNum')
        cla_room_num = req.POST.get('claRoomNum')
        cla_longitude = req.POST.get('claLongit')
        cla_latitude = req.POST.get('claLatit')
        # print(cla_floor_num,cla_room_num,cla_longitude,cla_latitude)

        class_loca.Class_Floor_Number = cla_floor_num
        class_loca.Class_Room_Number = cla_room_num
        class_loca.Class_Latitude = cla_latitude
        class_loca.Class_Longitude = cla_longitude
        class_loca.save()
        messages.success(req, 'Clas Location was added Successfully..!')
        return redirect('teacher_add_class_location_form', id=id)
    
    return render(req, 'teacher/teacher-add-location-form.html')

# Teacher Attendace Details
def teacherAttendanceDetails(req):
    classes = Classes_Coducted_Model.objects.all().order_by('Cl_Date')
    paginator = Paginator(classes, 5) 
    page_number = req.GET.get('page')
    post = paginator.get_page(page_number)
    return render(req, 'teacher/teacher-attendance-details.html', {'a' : post} )

def teacherGraph(req, id):
    # print(id)
    cla_info = Classes_Coducted_Model.objects.get(Cla_Id = id)
    # print(cla_info, 'cla_id')
    stu_atten = Attendance_Details_Model.objects.filter(Att_Date = cla_info.Cl_Date, Student_Subject = cla_info.Subject, Student_Branch = cla_info.Branch, Student_Section = cla_info.Section)
    # print(stu_atten)
    stu_present = Attendance_Details_Model.objects.filter(Att_Date = cla_info.Cl_Date, Student_Subject = cla_info.Subject, Student_Branch = cla_info.Branch, Student_Section = cla_info.Section, Att_Status = 'present').count()
    print(stu_present)
    stu_info = Student_Details_Model.objects.filter(Student_Branch = cla_info.Branch, Student_Section = cla_info.Section).count()
    # print(stu_info)
    stu_absent = stu_info - stu_present
    class_name = cla_info.Subject
    class_date = cla_info.Cl_Date
    # print(stu_info, stu_present, stu_absent)
    return render(req, 'teacher/teacher-graph.html', {'stu_att': stu_atten ,'t' : stu_info, 'p' : stu_present, 'a' : stu_absent, 'cn' : class_name, 'cd' : class_date})

# Teacher Student Statistics Details
def teacherStudentStatistic(req, id):
    stu_info = Student_Details_Model.objects.get(Student_Id = id)
    cla_info = Classes_Coducted_Model.objects.filter(Branch = stu_info.Student_Branch, Section = stu_info.Student_Section).count()
    att_info_present = Attendance_Details_Model.objects.filter(Student_Name = stu_info.Student_Name, Student_Branch = stu_info.Student_Branch, Student_Section = stu_info.Student_Section, Att_Status = 'present').count()
    att_info_absent = Attendance_Details_Model.objects.filter(Student_Name = stu_info.Student_Name, Student_Branch = stu_info.Student_Branch, Student_Section = stu_info.Student_Section,  Att_Status = 'absent').count()
    atten_info = Attendance_Details_Model.objects.filter(Student_Name = stu_info.Student_Name, Student_Branch = stu_info.Student_Branch, Student_Section = stu_info.Student_Section)
    return render(req, 'teacher/teacher-student-statistics.html', {'sn' : stu_info.Student_Name, 'cc' : cla_info, 'cp' : att_info_present, 'ca' : att_info_absent, 'att_info' : atten_info})

# Teacher Record Attendance
def teacherRecordAttednace(req):
    classes = Class_Details_Model.objects.filter(Class_Latitude__gt = 0).order_by('Class_Start_Time')
    paginator = Paginator(classes, 5) 
    page_number = req.GET.get('page')
    post = paginator.get_page(page_number)
    return render(req, 'teacher/teacher-record-attendance.html', {'cla' : post})

# QR COde Start button
def startQRBtn(req, id):
    class_qr = Class_Details_Model.objects.get(Class_Id = id)
    # print(class_qr)
    student = Student_Details_Model.objects.filter(Student_Branch = class_qr.Branch_Name, Student_Section = class_qr.Section)
    t = time.localtime()
    # print(t, 'hello time')
    class_qr.Class_Date = t
    current_date = time.strftime('%Y-%m-%d')
    class_qr.Class_Date = current_date
    class_qr.save()
    # yyyy = class_qr.Class_Start_Time.strftime("%H:%M:%S")
    # xxxx = class_qr.Class_End_Time.strftime("%H:%M:%S")

    data = {
        'Institute Name' : 'sreyas institute of engineering and technology',
        'Incharge Name': class_qr.Class_Incharge_Name,
        'Branch Name': class_qr.Branch_Name,
        'Section': class_qr.Section,
        'Subject' : class_qr.Subject_Name,
        'Class Date' : class_qr.Class_Date,
        'Class Duration' : class_qr.Class_Duration,
        'Class Start Time' : class_qr.Class_Start_Time,
        'Class End Time' : class_qr.Class_End_Time,
        'Class Floor Number' : class_qr.Class_Floor_Number,
        'Class Room Number' : class_qr.Class_Room_Number
    }
    # Create the data string with line breaks
    data_string = '\n'.join([f"{key}: {value}" for key, value in data.items()])
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    # Add the data string to the QR code
    qr.add_data(data_string)
    # Compile the QR code
    qr.make(fit=True)
    # Create an image from the QR code
    qr_image = qr.make_image(fill_color="black", back_color="white")
    a=qr_image
    ImageDraw.Draw(a)
    a.paste(qr_image)
    buffer=BytesIO()
    a.save(buffer,"PNG")
    class_qr.Class_QR_Code = f'images/cla_qr/{class_qr.Subject_Name + class_qr.Section}.png'
    class_qr.Class_QR_Code.save(f'{class_qr.Subject_Name + class_qr.Section}.png', File(buffer),save=False)
    a.close()
    # Save the image
    # print(qr_image, 'helllllooooooooooo')
    # Data for QR Code
    # data =  class_qr.Branch_Name +' '+  class_qr.Section +' ' + class_qr.Class_Incharge_Name + ' ' + class_qr.Subject_Name + ' ' + class_qr.Class_Date + ' ' + class_qr.Class_Duration + ' ' + yyyy + ' ' + xxxx
    # # Making QR Code
    # qrcode_img=qrcode.make({data})
    # canvas=Image.new("RGB", (500,500),"white")
    # ImageDraw.Draw(canvas)
    # canvas.paste(qrcode_img)
    # buffer=BytesIO()
    # canvas.save(buffer,"PNG")
    # class_qr.Class_QR_Code = f'images/cla_qr/{data}.png'
    # class_qr.Class_QR_Code.save(f'{data}.png', File(buffer),save=False)
    # # print(qrcode_img)
    # canvas.close()
    class_qr.Class_QR_Status = 'active'
    class_qr.Class_Count += 1
    class_qr.save() 
    for i in student:
        i.Class_Subject = class_qr.Subject_Name
        i.Class_Date = class_qr.Class_Date
        i.Class_Inch_Name = class_qr.Class_Incharge_Name
        i.Class_Time = class_qr.Class_Start_Time
        i.save()
    Classes_Coducted_Model.objects.create(Cla_Foregin = class_qr, Branch = class_qr.Branch_Name, Section = class_qr.Section, Subject = class_qr.Subject_Name, Cl_Date = class_qr.Class_Date, Cl_Time = class_qr.Class_Start_Time, Class_Inch = class_qr.Class_Incharge_Name)
    messages.success(req, 'Class was Started and QR Codes sent to Students Successfully..!')
    return redirect('teacher_record_attendance')

# QR Code End button
def endQRBtn(req, id):
    class_qr = Class_Details_Model.objects.get(Class_Id = id)
    class_qr.Class_QR_Status = 'deactive'
    
    student = Student_Details_Model.objects.filter(Student_Branch = class_qr.Branch_Name, Student_Section = class_qr.Section, Class_Subject = class_qr.Subject_Name)
    # (i.Class_Subject == class_qr.Subject_Name) and
    for i in student:
        if (i.Student_QR_Status == 'not-uploaded'):
            Attendance_Details_Model.objects.create(Stu_Foregin_id = i.Student_Id, Cla_Foregin_id = class_qr.Class_Id, Student_Name = i.Student_Name, Student_Branch = i.Student_Branch, Student_Subject = i.Class_Subject, Student_Section = i.Student_Section, Student_Rollnum = i.Student_RollNumber, Att_Date = i.Class_Date, Att_Status = 'absent', Class_Incharge = i.Class_Inch_Name, Class_Time = i.Class_Time)
        i.Class_Subject = ""
        i.Student_QR_Status = 'not-uploaded'
        i.save()
    
    class_qr.save()
    messages.warning(req, 'Class was Ended..!')
    return redirect('teacher_record_attendance')

# Edit Class Location
def teacherEditLocation(req, id):
    cla_info = Class_Details_Model.objects.get(Class_Id = id)
    if req.method == 'POST' :
        flo_nm = req.POST.get('floNum')
        room_num = req.POST.get('roomNum')
        lati = req.POST.get('lati')
        long = req.POST.get('long')
        if len(req.FILES) != 0:
            cla_info.Class_Floor_Number = flo_nm
            cla_info.Class_Room_Number = room_num
            cla_info.Class_Latitude = lati
            cla_info.Class_Longitude = long
            cla_info.save()
        else:
            cla_info.Class_Floor_Number = flo_nm
            cla_info.Class_Room_Number = room_num
            cla_info.Class_Latitude = lati
            cla_info.Class_Longitude = long
            cla_info.save()
        return redirect('teacher_edit_class_location', id = id)
    return render(req, 'teacher/teacher-edit-class-location.html', {'x' : cla_info})

# Delete class
def deleteBtn(req, id):
    class_qr = Class_Details_Model.objects.get(Class_Id = id)
    class_qr.delete()
    messages.warning(req, 'Clas was Deleted Suceessfully..!')
    return redirect('teacher_record_attendance')

# Teacher Statistics Analysis
def teacherStatisticsAnalysis(req):
    all_students = Student_Details_Model.objects.all().order_by('Student_Id')
    paginator = Paginator(all_students, 5) 
    page_number = req.GET.get('page')
    post = paginator.get_page(page_number)
    return render(req, 'teacher/teacher-statistics-analysis.html', {'x' : post})

# Teacher Grapth Analysis
# def teacherGraphAnalysis(req):
#     cla_details = Class_Details_Model.objects.all()
#     return render(req, 'teacher/teacher-graph-analysis.html', {'cl':cla_details})

# Teacher Load Balancing
def teacherLoadBalancing(req):
    atten_deatils = Attendance_Details_Model.objects.filter(Att_Status = 'present')
    paginator = Paginator(atten_deatils, 5) 
    page_number = req.GET.get('page')
    post = paginator.get_page(page_number)
    return render(req, 'teacher/teacher-load-balancing-details.html', {'att' :post})

# Teacher Logout
def teacherLogout(req):
    messages.info(req, 'Logout Successfully..!')
    return render(req, 'main/main-teacher-login.html')

