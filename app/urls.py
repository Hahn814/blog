from django.urls import path
from blog.views import home as blog_home

urlpatterns = [
    path('', blog_home, name='app-home'),
]
