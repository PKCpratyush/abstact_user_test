from django.shortcuts import render
from .models import New_user, Custom_manager

# Create your views here.

def index(request):
    return render(request, 'index.html',{"session_exist": False})

def saveit(request):
    if 'name' in request.session:
        return render(request, 'index.html',{"session_exist": True, "name" : request.session.get('name')})

    user_name = request.GET.get("user_name",'')
    password = request.GET.get("password",'')

    request.session['name'] = user_name

    # user = New_user(user_name = name, password = password, is_staff = True, is_active = True, is_superuser = True)
    # user.save()
    user = New_user(user_name = user_name, password = password, is_staff = True, is_active = True)
    user.save()
    user_name = ""
    password = ""
    return render(request, 'index.html',{"session_exist": True, "name" : request.session.get('name')})


def session_delete(request):
    if 'name' in request.session:
        del request.session['name']
    return render(request, 'index.html', {"session_exist": False})