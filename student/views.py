from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import Student_table
from .forms import Studentform_data
def home(request):
    data1={
        'name':"Pratiksha",
        'age':19,
        'department':"BCA"
    }
    marks=[100,99,98]
    return render(request, 'home.html',{'data1':data1, 'marks1':marks})
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
def forms1(request):
    if request.method=="POST":
        reg_no=request.POST.get('reg_no')
        name=request.POST.get('name') 
        marks=request.POST.get('marks')
        email=request.POST.get('email')
        date=request.POST.get('dob')
        Student_table.objects.create(
            reg_no=reg_no,
            name=name,
            email=email,
            marks=marks,
            date=date,
        )
        return HttpResponse("saved successfully!!")
    return render(request,'studentform.html')

def student_form_dj(request):
    if request.method == "POST":
        form = Studentform_data(request.POST)

        if form.is_valid():
            reg_no1 = form.cleaned_data['reg_no1']
            name1 = form.cleaned_data['name1']
            email1 = form.cleaned_data['email1']

            return HttpResponse("Saved successfully!!")
        else:
            return HttpResponse("Invalid Data")

    else:
        form = Studentform_data()

    return render(request, 'studentfrom_data.html', {'form': form})