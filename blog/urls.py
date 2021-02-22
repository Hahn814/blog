from django.urls import path
from blog import views
from blog.views.posts import PostView

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/', PostView.as_view(), name='post-view')
]
