# -*- coding: utf-8 -*-

# Django
from django.shortcuts import render
from users.models import BlogUserProfile

def home(request):
    title = 'Users Home'

    context = {
        'user_profiles': BlogUserProfile.objects.all().order_by('-id'),
        'title': title
    }
    return render(request=request, template_name='users/home.html', context=context)

def view_blog_user_profile(request, user_id):
    profile = BlogUserProfile.objects.get(user__id=user_id)

    context = {
        'user_profile': profile
    }
    return render(request=request, template_name='users/profile.html', context=context)