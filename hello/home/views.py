from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
 
# Create your views here.
def index(request):
   
    return render(request,"index.html")

    messages.success(request,"this is a test message")
def about(request):
    # return HttpResponse("this is about page")
     return render(request,"about.html")
def services(request):
    # return HttpResponse("this is services page")
     return render(request,"services.html")
def contact(request):
    # return HttpResponse("this is contact page")
     if request.method == "POST":
         password = request.POST.get('password')
         email = request.POST.get('email')
        #  date = datetime.today()
         contact = Contact(email=email,password=password)
         contact.save()
         messages.success(request, "Profile details are submitted")


     return render(request,"contact.html")