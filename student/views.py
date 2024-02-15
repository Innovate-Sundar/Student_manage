from django.shortcuts import render,redirect
from . models import Student

# Create your views here.

def home(request):
    std=Student.objects.all()

    return render(request,'student/home.html',{'std':std})

def std_add(request):
    if request.method=='POST':
        print('Added')
        #retreive the student inputs
        stds_rollno=request.POST.get("std_rollno")
        stds_name=request.POST.get("std_name")
        stds_degree=request.POST.get("std_degree")
        stds_department=request.POST.get("std_department")
        stds_email=request.POST.get("std_email")
        stds_address=request.POST.get("std_address")
        stds_phone=request.POST.get("std_phone")

        #create an object for models
        s=Student()
        s.rollno=stds_rollno
        s.name=stds_name
        s.degree=stds_degree
        s.department=stds_department
        s.email=stds_email
        s.address=stds_address
        s.phone=stds_phone

        s.save()
        return redirect("/student/home")
    
    return render(request,'student/add_std.html',{})

def delete_std(request,rollno):
    s=Student.objects.get(pk=rollno)
    s.delete()

    return redirect("/student/home")

def update_std(request,rollno):
    std=Student.objects.get(pk=rollno)

    return render(request,"student/update_std.html",{'std':std})

def do_update_std(request,rollno):
    std_rollno=request.POST.get("std_rollno")
    std_name=request.POST.get("std_name")
    std_degree=request.POST.get("std_degree")
    std_department=request.POST.get("std_department")
    std_email=request.POST.get("std_email")
    std_address=request.POST.get("std_address")
    std_phone=request.POST.get("std_phone")

    std=Student.objects.get(pk=rollno)

    std.rollno=std_rollno
    std.name=std_name
    std.degree=std_degree
    std.department=std_department
    std.email=std_email
    std.address=std_address
    std.phone=std_phone

    std.save()
    return redirect("/student/home")