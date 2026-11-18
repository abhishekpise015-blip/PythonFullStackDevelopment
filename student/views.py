from django.shortcuts import render
def home(request):
    data1={
        'name':"Abhishek",
        'age':19,
        'department':"BCA"
    }
    marks=[100,99,98]
    return render(request, 'home.html',{'data1':data1, 'marks1':marks})
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')