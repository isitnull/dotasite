from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'dotasite/index.html')


def auth_login(request):
    if request.method == "POST":
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        if username and password:
            print username
            print password
            user = authenticate(username=username, password=password)
            if user:
                print user
                if user.is_active:
                    print 'yes!'
                    login(request, user)

    return redirect(reverse('dotasite.views.index'))


def auth_logout(request):
    logout(request)
    return redirect(reverse('dotasite.views.index'))


def challenge(request):
    return render(request, 'dotasite/challenge.html')
