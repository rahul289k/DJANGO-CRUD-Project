from django.shortcuts import redirect, render
from .forms import UserRegistration
from .models import User
from django.http import HttpResponseRedirect


def add_show(request):
    if request.method == "POST":
        obj = UserRegistration(request.POST)
        if obj.is_valid():
            obj.save()
            obj = UserRegistration()
    else:
        obj = UserRegistration()
    stu = User.objects.all()
    return render(request, 'enroll/addandshow.html', {"data": obj,"stu":stu})
# Create your views here.

def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk = id)
        pi.delete()
        return HttpResponseRedirect("/")


def update_data(request,id):
    if request.method =='POST':
        pi = User.objects.get(pk=id)
        fm = UserRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()

    else:
        pi = User.objects.get(pk=id)
        fm = UserRegistration(instance=pi)

    return render(request,'enroll/update.html',{'updated':fm})

