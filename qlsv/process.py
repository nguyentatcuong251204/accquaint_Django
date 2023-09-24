from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from qlsv.models import Students,ids
from django.contrib import messages
from django.db import models
     
def add_student_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        name=request.POST.get('name')
        gender=request.POST.get('gender')
        
        try:
            user = Students(name=name, gender=gender)    
            user=user.save()                    
            messages.success(request, "Successfully Added Student")
            # return HttpResponseRedirect(reverse("add_student"))
            return render(request,'holdtemplate/add_student.html')
            
        except:
            messages.error(request, "ss")
            # return HttpResponseRedirect(reverse("add_student"))
            return render(request,'holdtemplate/add_student.html')

def display(request):
    students=Students.objects.all()
    return render(request,'holdtemplate/manage_student.html',{'students':students})

def displaydb(request):
    students=Students.objects.all()
    student=students.get(id=1)
    id=student.id
    # return render(request,'holdtemplate/displaydb.html',{'students':students})
    return HttpResponse(id)



def setting(request):
    id=request.POST.get('id')
    student=Students.objects.get(id=id)
    name=student.name
    gender=student.gender
    return render(request,'holdtemplate/setting.html',{'name':name,'gender':gender})

def edit(request):
    id=request.POST.get('id')
    return render(request,'holdtemplate/edit.html',{'id':id})


def edit_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        students=Students.objects.all()
        name=request.POST.get('name')
        gender=request.POST.get('gender')
        id=request.POST.get('id')    
        student=Students.objects.get(id=id)
        student.name=name
        student.gender=gender
        student.save()
        
        return render(request,'holdtemplate/manage_student.html',{'students':students})
        # return HttpResponse(student.gender)
        
            
def delete(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        students=Students.objects.all()
        id=request.POST.get('id')
        student=Students.objects.get(id=id)
        student.delete()
        return render(request,'holdtemplate/manage_student.html',{'students':students})



    
