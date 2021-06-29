
from django.urls import path

from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('<int:blogid>/', views.detail, name='detail'),
    
] 
