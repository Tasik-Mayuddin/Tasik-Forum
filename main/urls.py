from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('search=<str:word>', views.search, name = 'search'),
    path('threads/<int:id>', views.index, name = 'index'),
    path('profile', views.profile, name = 'profile'),
    path('userposts/<str:uname>', views.userposts, name = 'userposts'),
]

