from django.shortcuts import render , HttpResponse
from hello.models import About

def index(request):
    if request == "POST":
        email= request.POST.get('email')
        email2= request.POST.get('email2')
        about= About(email=email,email2=email2)
        about.save()
    
    return render(request, 'index.html')
# Create your views here.
def introduction(request):
    return render(request,'introduction.html')
def About(request):
    return render(request, 'About.html')
