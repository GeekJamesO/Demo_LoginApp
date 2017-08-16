# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from models import User

# Create your views here.
def index(request):
    context = { }
    return render(request, "login_app/index.html", context)

def register(request):
    print User.objects.RegVal(request.POST)
    return render(request, "login_app/index.html")
