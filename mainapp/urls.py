from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('category/', views.category, name='category'),
    path('district/', views.district, name='districts'),
    path('township/', views.township, name='townships'),
    path('village/', views.village, name='villages'),
    path('ward/', views.ward, name='wards'),
    path('township_detail/', views.township_detail, name='township_detail'),
]
