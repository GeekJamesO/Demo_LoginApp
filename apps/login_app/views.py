# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.
def index(request):
    context = { }
    return render(request, "login_app/index.html", context)

def register(request):
    print "in register"
    print request.POST
    print "First name:" , request.POST['first_name']

    return render(request, "login_app/index.html")
