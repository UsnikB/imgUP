from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.user_logout, name='logout'),
    path('login/', views.UserLogin.as_view() , name='login'),
    path('user/<str:username>/', views.UserProfile.as_view(), name='user_profile'),
]
