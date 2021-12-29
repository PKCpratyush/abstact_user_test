from django.shortcuts import render
from .models import New_user

# Create your views here.

def index(request):
    return render(request, 'index.html')

def saveit(request):
    name = request.GET.get("name",'')
    password = request.GET.get("password",'')

    user = New_user(user_name = name, password = password)
    user.save()

    return render(request, 'index.html')