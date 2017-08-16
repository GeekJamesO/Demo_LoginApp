# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from models import User
from django.contrib import messages
import bcrypt


# Create your views here.
def index(request):
    context = { }
    return render(request, "login_app/index.html", context)

def register(request):
    results = User.objects.RegVal(request.POST)
    if results['status'] == False:
        for msg in results['errors']:
            messages.error(request, msg)
        return redirect('/')
    User.objects.Creator(request.POST)
    return redirect("/")

def login(request):
    results = User.objects.logVal(request.POST)
    if results['status'] == False:
        for msg in results['errors']:
            messages.error(request, msg)
        return redirect("/")
    request.session['user_id'] = results['user'].id
    request.session['user_first_name'] = results['user'].first_name
    request.session['user_last_name'] = results['user'].last_name
    request.session['user_email'] = results['user'].email
    # not going to store hashed password...
    print ''
    return redirect("/home")
