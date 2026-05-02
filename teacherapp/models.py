from django.db import models

# Create your models here.
class Student_Details_Model(models.Model):
    Student_Id = models.AutoField(primary_key = True)
    Student_Name = models.TextField(max_length = 50)
    Student_Age = models.IntegerField(null = True)
    Student_Email = models.EmailField(max_length=100)
    Student_Phone_Number = models.TextField(max_length = 10, null = True)
    Student_RollNumber = models.TextField(max_length = 20, null = True)
    Student_Address = models.TextField(max_length = 200, null = True)
    Student_Branch = models.TextField(max_length = 10, null = True)
    Student_Section = models.TextField(max_length = 4, null = True)
    Student_Gender = models.TextField(max_length = 10, null = True)
    Student_Profile = models.FileField(upload_to = 'images/')
    Student_Status = models.TextField(default = 'pending')
    Student_Password = models.TextField(null = True)
    Student_Last_Login_Time = models.TimeField(null = True)
    Student_Last_Login_Date = models.DateField(null = True)
    Student_Last_Logout_Time = models.TimeField(null = True)
    Student_No_Of_Times_Login = models.IntegerField(default = 0, null = True)
    Student_No_Of_Times_Logout = models.IntegerField(default = 0, null = True)
    Student_Online_Status = models.TextField(default = 'offline')
    Student_Upload_QR_Codes = models.FileField(upload_to = 'images/stu_qr/', null = True)
    Class_Subject = models.TextField(null = True)
    Student_QR_Code_Upload_Time = models.TimeField(null = True)
    Student_QR_Code_Upload_Date = models.DateField(null = True)
    Student_QR_Status = models.TextField(default = 'not-uploaded')
    Student_Latitude = models.FloatField(null = True)
    Student_Longitude = models.FloatField(null = True)
    Class_Date = models.DateField(null = True)
    Class_Inch_Name = models.TextField(null = True)
    Class_Time= models.TimeField(null = True)

    class Meta:
        db_table = 'student_details'


        
class Class_Details_Model(models.Model):
    Class_Id = models.AutoField(primary_key = True)
    Class_Incharge_Name = models.TextField(max_length = 50)
    Subject_Name = models.TextField(max_length = 20, null = True)
    Branch_Name = models.TextField(max_length = 20)
    Section = models.TextField(max_length = 10)
    Class_Start_Time = models.TimeField(null = True)
    Class_End_Time = models.TimeField(null = True)
    Class_Duration = models.TextField(max_length = 20)
    Class_Floor_Number = models.TextField(max_length = 10, null = True)
    Class_Room_Number = models.TextField(max_length = 10, null = True)
    Class_Latitude = models.FloatField(null = True)
    Class_Longitude = models.FloatField(null = True)
    Class_QR_Code = models.FileField(upload_to = 'images/cla_qr/', null = True)
    Class_QR_Status = models.TextField(default = 'deactive')
    # Class_Status = models.TextField(default = 'deactive')
    Class_Date = models.DateField(null = True)
    Class_Count = models.IntegerField(default = 0)
    Student_Details_Foregin = models.ForeignKey(Student_Details_Model, related_name='students_in_class', on_delete = models.CASCADE, null = True )

    class Meta:
        db_table = 'class_details'

class Attendance_Details_Model(models.Model):
    Att_Id = models.AutoField(primary_key = True)
    Student_Name = models.TextField(max_length = 50)
    Student_Branch = models.TextField(max_length = 50)
    Student_Subject = models.TextField(max_length = 100)
    Student_Section = models.TextField(max_length = 20)
    Student_Rollnum = models.TextField(max_length = 20)
    Att_Date = models.DateField(null = True)
    Att_Status = models.TextField(default = 'absent') 
    Cpu = models.TextField(null = True)
    Ram = models.TextField(null = True)
    HardDisk = models.TextField(null = True)
    Class_Incharge = models.TextField(max_length = 100, null = True)
    Class_Time = models.TimeField(null = True)
    QR_Time = models.TimeField(null = True)
    Stu_Foregin = models.ForeignKey(Student_Details_Model, on_delete = models.CASCADE, null = True )
    Cla_Foregin = models.ForeignKey(Class_Details_Model, on_delete = models.CASCADE, null = True )

    class Meta:
        db_table = 'attendance_details'

class Classes_Coducted_Model(models.Model):
    Cla_Id = models.AutoField(primary_key = True)
    Class_Inch = models.TextField(max_length = 100, null = True)
    Branch = models.TextField(max_length = 50)
    Section = models.TextField(max_length = 50)
    Subject = models.TextField(max_length = 100)
    Cl_Date = models.DateField(null = True)
    Cl_Time = models.TimeField(null = True)
    Stu_Foregin = models.ForeignKey(Student_Details_Model, on_delete = models.CASCADE, null = True )
    Cla_Foregin = models.ForeignKey(Class_Details_Model, on_delete = models.CASCADE, null = True )
    Atten_Foregin = models.ForeignKey(Attendance_Details_Model, on_delete = models.CASCADE, null = True )

    class Meta:
        db_table = 'classes_conduct'