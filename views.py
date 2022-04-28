from django.http import HttpResponse,HttpResponseRedirect

from django.shortcuts import render
from django.http import HttpResponse

from enrol.forms import StudentRegiration
from .models import User
# Create your views here.

def add_show(request):
    if request.method=="POST":
        fm=StudentRegiration(request.POST)
        if fm.is_valid():
            fm.save()
        fm=StudentRegiration()
    else:
        fm=StudentRegiration()
    stud=User.objects.all()
        
    return render(request,'enrool/addandshow.html',{'form':fm,'stu':stud})

def delete_data(request,id):
    if request.method=="POST":
        user_delete=User.objects.get(pk=id)
        user_delete.delete()
        return HttpResponseRedirect('/')
        
def update_data(request,id):
    if request.method=="POST":
        user_info=User.objects.get(pk=id)
        fm=StudentRegiration(request.POST,instance=user_info)
        
        if fm.is_valid():
            fm.save()
    else:
        user_info=User.objects.get(pk=id)
        fm=StudentRegiration(instance=user_info)
    
    return render(request,'enrool/updatestudent.html',{'form':fm})
    
        

