from django.shortcuts import render
from qlsv.models import Students
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib import messages
def form(request):
    return render(request,'html.html')



