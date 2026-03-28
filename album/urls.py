from django.urls import path
from . import views

urlpatterns = [
    path('', views.photo_list, name='home'),
    path('upload/', views.photo_upload, name='upload'),
    path('delete/<int:pk>/', views.photo_delete, name='photo_delete'),
    path('photo/<int:pk>/', views.photo_detail, name='photo_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]