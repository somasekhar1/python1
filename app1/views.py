import csv
from django.shortcuts import render
from .models import courses
from django.http import HttpResponse
from .models import student
from firebase import firebase as fab
fa=fab.FirebaseApplication("https://django5-27d69.firebaseio.com/",None)
from .models import faculty

def display(request):
    return render(request,"display.html")


def head(request):
    return render(request,"head.html")


def menu(request):
    return render(request,"menu.html")


def adminlogin(request):
    return render(request,"admin login.html")


def adminlogindetails(request):
    uname=request.POST.get("name")
    upass=request.POST.get("password")
    if uname=="admin" and upass=="admin":
          return render(request,"admin_home.html")
    else:
        return render(request,"admin login.html",{"msg":"invalid user"})


def course(request):
    res=courses.objects.all()
    return render(request,"view course.html",{"msg":res})


def addcourse(request):
    return render(request,"add course.html")


def addcoursedetails(request):
    c_name=request.POST.get("name")
    c_id=request.POST.get("cid")
    c_fee=request.POST.get("cfee")
    c_duration=request.POST.get("cdur")
    c1=courses(coursename=c_name,courseid=c_id,coursefee=c_fee,courseduration=c_duration)
    c1.save()
    return render(request,"add course.html",{"res":"registered your course cuccessfully"})


def coursedelete(request):
    id=request.POST.get("delete_id")
    courses.objects.filter(courseid=id).delete()
    courses.objects.all()
    return course(request)


def courseupdate(request):
    id=request.GET.get("update_id")
    courses.objects.filter(courseid=id).update()
    return render(request,"add course.html",{"id":id})


def coursecsv(request):
    response=HttpResponse(content_type="text/csv")
    response['Content-Disposition']='attachment';filename="course.csv"
    wr=csv.writer(response)
    cl=courses.objects.all()
    for x in cl:
        wr.writerow([x.coursename,x.courseid,x.coursefee,x.courseduration])
    return response

def student1(request):
    d=student.objects.all()
    return render(request,"view_student_details.html",{"stu":d})

def viewstudent(request):

    return render(request,"student_register.html")


def studentdetails(request):
    sname=request.POST.get("s1")
    scontact=request.POST.get("s2")
    sgender=request.POST.get("s3")
    susername=request.POST.get("s4")
    spassword=request.POST.get("s5")
    semail=request.POST.get("s6")
    s1=student(name=sname,contect=scontact,gender=sgender,username=susername,password=spassword,email=semail)
    print(s1)
    s1.save()
    return render(request,"student_register.html",{"res":"registration successfully"})


def studentlogin(request):
    return render(request,"student login.html")


def studentlogindetails(request):
    s_name=request.POST.get("u1")
    s_pass=request.POST.get("u2")
    login=student.objects.filter(username=s_name,password=s_pass)
    if not login:
        return render(request,"student login.html",{"msg2":"invalid details"})
    else:
        return render(request,"student welcome page.html")


def studentwelcomedetails(request):
    sd1=request.POST.get("a1")
    sd2=request.POST.get("a2")
    sd3=request.POST.get("a3")
    sd4=request.POST.get("a4")
    sd5=request.POST.get("a5")
    d1={"name":sd1,"qualification":sd3,"course":sd4,"timing":sd5}
    fa.put("details",sd2,d1)
    return render(request,"student welcome page.html",{"status":"successfuly saved to firebase"})


def studentcsv(request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment'; filename = "student.csv"
    wr = csv.writer(response)
    cl = student.objects.all()
    for x in cl:
        wr.writerow([x.name, x.contect, x.gender, x.username, x.password, x.email])
    return response


def  faculty1(request):
    return render(request,"add faculty.html")


def facultydetails(request):
    fct1=request.POST.get("f1")
    fct2=request.POST.get("f2")
    fct3=request.POST.get("f3")
    fct4=request.POST.get("f4")
    fct5=request.POST.get("f5")
    fct6=request.POST.get("f6")
    fct7=request.POST.get("f7")
    fct8=request.POST.get("f8")
    f1=faculty(id=fct1,name=fct2,contact=fct3,gender=fct4,username=fct5,password=fct6,email=fct7,course=fct8)
    f1.save()
    return render(request,"add faculty.html",{"fact":"successfully saved"})


def viewsfaculty(request):
    f=faculty.objects.all()
    return render(request,"view faculty.html",{"fac":f})


def facultydelete(request):
    facd=request.POST.get("del")
    faculty.objects.filter(id=facd).delete()
    faculty.objects.all()
    return viewsfaculty(request)


def facultyupdate(request):
    fid=request.GET.get("fac_update")
    print(fid)
    faculty.objects.filter(id=fid).update()
    return render(request,"add faculty.html",{"fid":id})