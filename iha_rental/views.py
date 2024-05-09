from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate

def homePage(request):
    authenticate(request=request, username="admin", password="admin")
    return render(request, "index.html", {})
    

def registerPage(request):
    return render(request, "register.html", {})

def loginPage(request):
    return render(request, "login.html", {})