# -*- coding: utf-8 -*-

# Django
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Blog Home</h1>')