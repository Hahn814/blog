# -*- coding: utf-8 -*-

# Django
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Users Home</h1>')