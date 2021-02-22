# -*- coding: utf-8 -*-

# Django
from django.shortcuts import render
from blog.models import BlogPost


def home(request):
    title = 'Home'
    posts = BlogPost.objects.all().order_by('-id')[:10]

    context = {
        'posts': posts,
        'title': title
    }
    return render(request=request, template_name='blog/home.html', context=context)


def about(request):
    title = 'About'

    context = {
        'title': title
    }
    return render(request=request, template_name='blog/about.html', context=context)
