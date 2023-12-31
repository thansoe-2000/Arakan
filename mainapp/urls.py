from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    
    path('district/', views.district, name='districts'),
    path('township/', views.township, name='townships'),
   
    path('township_detail/<str:pk>/', views.township_detail, name='township_detail'),
    path('district_detail/<str:pk>/', views.district_detail, name='district_detail'),
]
