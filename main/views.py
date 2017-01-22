from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from connection import request_get, request_post

DEFAULT_URL = 'http://localhost:8000'

def index_view(request):
    if request.method == "GET":
        if request.session.get('user'):
            return render(request, 'index.html')
        else:
            return redirect('/login/')
    else:
        raise Exception("POST")


def login_view(request):
    if request.method == "GET":
        if request.user.is_authenticated():
            return redirect('/')
        else:
            return render(request, 'login.html')
    else:
        login = request.POST.get('username')
        password = request.POST.get('password')
        res = request_post(request, DEFAULT_URL + '/api/login/', {'username': login, 'password': password})
        if res.get('result'):
            request.session['user'] = login
            request.session['role'] = res.get('role')
        if res.get('result'):
            return redirect('/')
        elif 'req_fields' in res:
            return render(request, 'login.html', {'error': 'Fields are required'})
        else:
            return render(request, 'login.html', {'error': 'Invalid login data'})

def logout(request):
    res = request_post(request, DEFAULT_URL + '/api/logout/')
    return redirect('/')

def count_clients_view(request):
    res = request_get(DEFAULT_URL + '/api/count-clients/')
    return render(request, 'count_clients.html', {res: res})