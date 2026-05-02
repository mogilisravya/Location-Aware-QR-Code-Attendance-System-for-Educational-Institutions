from django.shortcuts import render, redirect
from teacherapp.models import *
import time
from datetime import datetime
from django.contrib import messages
from AttendanceProject.settings import GOOGLE_MAP_API_KEY
import psutil
import shutil
from django.core.paginator import Paginator
from math import radians, sin, cos, sqrt, atan2
import math
from project_config.apps import LicenseGuardConfig
import cv2
import numpy as np

# Create your views here.

# Student Login
def studentLogin(req):
    if req.method == 'POST':
        stu_email = req.POST.get('stEmail')
        stu_pwd = req.POST.get('stPwd')
        try:
            stu_data = Student_Details_Model.objects.get(Student_RollNumber = stu_email, Student_Password = stu_pwd)
            stu_data.Student_No_Of_Times_Login += 1
            stu_data.Student_Online_Status = 'online'
            # print(stu_data.Student_No_Of_Times_Login)
            t = time.localtime()
            # print(t, 'hello time')
            stu_data.Student_Last_Login_Time = t
            current_time = time.strftime('%H:%M', t)
            stu_data.Student_Last_Login_Time = current_time
            stu_data.save()

            if stu_data.Student_Status == 'pending':
                req.session['Student_Id'] = stu_data.Student_Id
                return redirect('student_login')
            elif stu_data.Student_Status == 'rejected':
                req.session['Student_Id'] = stu_data.Student_Id
                return redirect('home')
            else:
                req.session['Student_Id'] = stu_data.Student_Id
                messages.success(req, 'Login Successfull..!')
                return redirect('student_dashboard')
            
        except:
            return redirect('student_login')

    return render(req, 'main/main-student-login.html')

# Student Forgot Password
def studentForgotPwd(req):
    return render(req, 'main/main-student-forgot-password.html')

# Student Dashboard
def studentDashboard(req):
    stu_id = req.session["Student_Id"]
    stu_info = Student_Details_Model.objects.get(Student_Id = stu_id)
    cla = Class_Details_Model.objects.filter(Branch_Name = stu_info.Student_Branch, Section = stu_info.Student_Section)
    # print(cla, 'classes count')
    atten_count = Attendance_Details_Model.objects.filter(Student_Rollnum = stu_info.Student_RollNumber, Att_Status = 'present').count()
    # print(atten_count, 'atten')
    classes_conduct = Classes_Coducted_Model.objects.all().count()
    try:
        z = 0
        for i in cla:
            z +=  i.Class_Count
        # print(z, "kknskjn")
        # print(z, 'final z')
        x = (atten_count/z)*100
        xyz = round(x, 2)
    except:
        xyz = 0
    # print(xyz)
    return render(req, 'student/student-dashboard.html', { 'x' : xyz, 'cc' : classes_conduct, 'cp' : atten_count, 'ca' : classes_conduct - atten_count})

# Student Profile
def studentProfile(req):
    stu_id = req.session['Student_Id']
    student = Student_Details_Model.objects.get(Student_Id = stu_id)
    context = {'i' : student}
    return render(req, 'student/student-profile.html', context)

# Student Attendance Details
def studentAttendaceDetails(req):
    student = req.session['Student_Id']
    stu_details = Student_Details_Model.objects.get(Student_Id = student)
    classes_details = Class_Details_Model.objects.filter(Branch_Name = stu_details.Student_Branch, Section = stu_details.Student_Section, Class_QR_Status = 'active' ).order_by('Class_Start_Time')
    return render(req, 'student/student-attendance-details.html', {'i' : classes_details})

# Student Record Attendacne
def studentRecordAttendace(req):
    student = req.session['Student_Id']
    stu_details = Student_Details_Model.objects.get(Student_Id = student)

    try:
        class_details = Class_Details_Model.objects.get(Branch_Name = stu_details.Student_Branch, Section = stu_details.Student_Section, Subject_Name = stu_details.Class_Subject)

    except:
        messages.info(req, 'Classes are not started...')

    if req.method == 'POST':
        stu_upload_qr_code = req.FILES['stupQrcode']
        stu_details.Student_Upload_QR_Codes = stu_upload_qr_code
        stu_details.save()
        
        # -------- QR Detection --------
        detector = cv2.QRCodeDetector()

        def decode_qr(image_path):
            """Robust QR code decoding using OpenCV only."""
            img = cv2.imread(image_path)
            if img is None:
                return None

            # Convert to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Try original color image
            data, _, _ = detector.detectAndDecode(img)
            if data:
                return data.strip()

            # Try grayscale image
            data, _, _ = detector.detectAndDecode(gray)
            if data:
                return data.strip()

            # Try adaptive thresholding
            thresh = cv2.adaptiveThreshold(
                gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                cv2.THRESH_BINARY, 11, 2
            )
            data, _, _ = detector.detectAndDecode(thresh)
            if data:
                return data.strip()

            # Try small rotations if still not detected
            for angle in [-15, -10, -5, 5, 10, 15]:
                (h, w) = gray.shape[:2]
                M = cv2.getRotationMatrix2D((w // 2, h // 2), angle, 1.0)
                rotated = cv2.warpAffine(gray, M, (w, h))
                data, _, _ = detector.detectAndDecode(rotated)
                if data:
                    return data.strip()

            return None


        # -------- Decode Class QR --------
        class_data = decode_qr(class_details.Class_QR_Code.path)
        if not class_data:
            messages.warning(req, "Class QR Code could not be detected!")
            return redirect('student_record_attendance')

        # -------- Decode Student QR --------
        student_data = decode_qr(stu_details.Student_Upload_QR_Codes.path)
        if not student_data:
            messages.warning(req, "Student QR Code could not be detected!")
            return redirect('student_record_attendance')

        x = class_data.strip()
        y = student_data.strip()
        lati = req.POST.get('latitude')
        long = req.POST.get('longitude')

        if not lati or not long or lati == "error" or long == "error":
            messages.warning(req, "Location not received properly. Enable GPS.")
            return redirect('student_record_attendance')

        try:
            lat1 = float(lati)
            lon1 = float(long)
        except ValueError:
            messages.warning(req, "Invalid location format.")
            return redirect('student_record_attendance')
        lat2 = class_details.Class_Latitude
        lon2 = class_details.Class_Longitude
        
        import math

        def calculate_distance(lat1, lon1, lat2, lon2):
            # Convert latitude and longitude from degrees to radians
            lat1_rad = math.radians(lat1)
            lon1_rad = math.radians(lon1)
            lat2_rad = math.radians(lat2)
            lon2_rad = math.radians(lon2)

            # Earth's radius in kilometers
            radius = 6371

            # Difference between latitudes and longitudes
            delta_lat = lat2_rad - lat1_rad
            delta_lon = lon2_rad - lon1_rad

            # Haversine formula
            a = math.sin(delta_lat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon / 2) ** 2
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

                # Calculate the distance
            distance = radius * c * 1000

            return distance

        # Calculate the distance
        result = calculate_distance(lat1, lon1, lat2, lon2)
        print("The distance between the two points is approximately:", round(result, 2), "m")
        abc = round(result, 2)
        print(abc,'aa')

        
        # Checking Time
        t = time.localtime()
        stu_details.Student_QR_Code_Upload_Time = t
        current_time = time.strftime('%H:%M', t)
        stu_details.Student_QR_Code_Upload_Time = current_time
        date_time_str = stu_details.Student_QR_Code_Upload_Time
        date_time_obj = datetime.strptime(date_time_str, '%H:%M').time()
        stu_details.Student_QR_Code_Upload_Time = date_time_obj
        
        stu_details.Student_QR_Code_Upload_Date = t
        current_date = time.strftime('%Y-%m-%d')
        stu_details.Student_QR_Code_Upload_Date = current_date
        date_time_str1 = stu_details.Student_QR_Code_Upload_Date
        date_time_obj1 = datetime.strptime(date_time_str1, '%Y-%m-%d').date()
        stu_details.Student_QR_Code_Upload_Date = date_time_obj1
        stu_details.save()
    
        # Allowed distance in meters
        allowed_distance = 100.0  # adjust as needed

        # Check Date
        if class_details.Class_Date == stu_details.Student_QR_Code_Upload_Date:

            # Check Time
            if class_details.Class_Start_Time <= stu_details.Student_QR_Code_Upload_Time <= class_details.Class_End_Time:

                # Check QR data match
                if x == y:

                    # Check Location
                    if abc <= allowed_distance:

                        # Check if QR already uploaded
                        if stu_details.Student_QR_Status == 'not-uploaded':

                            # Gather system info
                            aa = psutil.cpu_percent(4)
                            bb = psutil.virtual_memory()[2]
                            total, used, free = shutil.disk_usage("/")
                            cc = (" %d GiB" % (total // (2**30)))

                            # Create attendance record
                            Attendance_Details_Model.objects.create(
                                Stu_Foregin=stu_details,
                                Student_Name=stu_details.Student_Name,
                                Student_Rollnum=stu_details.Student_RollNumber,
                                Student_Section=stu_details.Student_Section,
                                Student_Branch=stu_details.Student_Branch,
                                Student_Subject=stu_details.Class_Subject,
                                Att_Date=stu_details.Student_QR_Code_Upload_Date,
                                QR_Time=stu_details.Student_QR_Code_Upload_Time,
                                Att_Status='present',
                                Cla_Foregin=class_details,
                                Class_Incharge=class_details.Class_Incharge_Name,
                                Class_Time=class_details.Class_Start_Time,
                                Cpu=aa,
                                Ram=bb,
                                HardDisk=cc
                            )

                            # Update student status
                            stu_details.Student_QR_Status = 'uploaded'
                            stu_details.save()

                            messages.success(req, 'QR Code was Uploaded Successfully..!')
                            return redirect('student_record_attendance')

                        else:
                            messages.warning(req, 'QR Code was Already Uploaded..!')
                            return redirect('student_record_attendance')

                    else:
                        messages.warning(req, f'QR Code Upload Location is incorrect!')
                        return redirect('student_record_attendance')

                else:
                    messages.warning(req, 'QR Code Data is incorrect..!')
                    return redirect('student_record_attendance')

            else:
                messages.warning(req, 'QR Code Upload Time is incorrect..!')
                return redirect('student_record_attendance')

        else:
            messages.warning(req, 'QR Code Upload Date is incorrect..!')
            return redirect('student_record_attendance')
    
    return render(req, 'student/student-record-attendance.html',{'a':GOOGLE_MAP_API_KEY})

# Student My Attendance Details
def studentMyAttendance(req):
    student = req.session['Student_Id']
    stu_details = Student_Details_Model.objects.get(Student_Id = student)
    atten_deatils = Attendance_Details_Model.objects.filter(Student_Rollnum = stu_details.Student_RollNumber).order_by('-Att_Date')
    paginator = Paginator(atten_deatils, 6) 
    page_number = req.GET.get('page')
    post = paginator.get_page(page_number)
    return render(req, 'student/student-my-attendance-details.html', {'abc' : post})

# Student Logout
def studentLogout(req):
    stu_id = req.session["Student_Id"]
    student = Student_Details_Model.objects.get(Student_Id = stu_id) 
    student.Student_No_Of_Times_Logout += 1
    student.Student_Online_Status = 'offline'
    t = time.localtime()
    # print(t, 'hello time')
    student.Student_Last_Logout_Time = t
    current_time = time.strftime('%H:%M', t)
    student.Student_Last_Logout_Time = current_time
    current_date = time.strftime('%Y-%m-%d')
    student.Student_Last_Login_Date = current_date
    student.save()
    # messages.info(req, 'You are logged out..')
    # print(student.Student_Last_Login_Time)
    # print(student.Student_Last_Login_Date)
    messages.info(req, 'Logout Successfully!')
    return redirect('student_login')
