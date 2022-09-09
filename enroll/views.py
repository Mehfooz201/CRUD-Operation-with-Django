from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.

# Add Data into the Table
def addShow(request):
    if request.method=='POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration() 
    else:
        fm = StudentRegistration()
    stud = User.objects.all()

    return render(request, 'enroll/addshow.html', {'form':fm, 'stu':stud})


def updateStudent(request):
    return render(request, 'enroll/updatestudent.html')



# Delete data from userINfo
def delDate(request, id):
    if request.method == 'POST':
        dt = User.objects.get(pk=id)
        dt.delete()

        return HttpResponseRedirect('/')



# Update Records from userINfo
def uptDate(request, id):
    if request.method == 'POST':
        upt = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=upt)
        if fm.is_valid():
            fm.save()

    else:
        upt = User.objects.get(pk=id)
        fm = StudentRegistration(instance=upt)

    return render(request, 'enroll/updatestudent.html', {'form':fm})