from django.shortcuts import render
from . models import *
# Create your views here.

def dashboard(request):
     districts = District.objects.all()
     townships = Township.objects.all()
     villages = Village.objects.all()
     context = {
          'districts':districts,
          'townships':townships,
          'villages':villages
     }
     return render(request, 'backend/layouts/dashboard.html', context)

def category(request):
     categories = Category.objects.all()
     context = {
          'categories':categories
     }
     return render(request, 'backend/pages/category.html', context)

def district(request):
     districts = District.objects.all()
     context = {
          'districts':districts,
     }

     return render(request, 'backend/pages/district.html', context)

def township(request):
     townships = Township.objects.all()
     context = {
          'townships':townships
     }
     return render(request, 'backend/pages/township.html', context)

def village(request):
     villages = Village.objects.all()
     context = {
          'villages':villages
     }
     return render(request, 'backend/pages/village.html', context)