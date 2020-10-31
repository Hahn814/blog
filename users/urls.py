from django.conf.urls import url
from django.urls import path
from users import views

urlpatterns = [
    path('', views.home, name='users-home'),
    url(r'profile/(?P<user_id>\d+)/', views.view_blog_user_profile, name='users-blog-user-profile'),
]
