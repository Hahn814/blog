# -*- coding: utf-8 -*-

# Django
from django.shortcuts import render

def home(request):
    title = 'Home'

    context = {
        'posts': [],
        'title': title
    }
    return render(request=request, template_name='blog/home.html', context=context)

def about(request):
    title = 'About'

    context = {
        'title': title
    }
    return render(request=request, template_name='blog/about.html', context=context)
