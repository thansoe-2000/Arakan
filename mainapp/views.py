from django.shortcuts import render
from . models import *
# Create your views here.

def dashboard(request):
     districts = District.objects.all()
     townships = Township.objects.all()
     
     context = {
          'districts':districts,
          'townships':townships,
          
     }
     return render(request, 'backend/layouts/dashboard.html', context)



def district(request):
     districts = District.objects.all()
     context = {
          'districts':districts,
     }

     return render(request, 'backend/pages/district.html', context)

def township(request):
    

     townships = Township.objects.all()
     context = {
          'townships':townships,
        
     }
     return render(request, 'backend/pages/township_detail.html', context)






def township_detail(request, pk=id):
     districts = District.objects.all()
     townships = Township.objects.all()
     
     township_townships = Township.objects.filter(district_id=pk)
     
     context = {
          'township_townships':township_townships,
          
          'districts':districts,
          'townships':townships,
          
     }
     return render(request, 'backend/pages/township_detail.html', context)


def district_detail(request, pk=id):
     districts = District.objects.all()
     townships = Township.objects.all()
    
     district_townships = Township.objects.filter(district_id=pk)
     
     context = {
          'districts':districts,
          'townships':townships,
          
          'district_townships':district_townships,
          
     }
     return render(request, 'backend/pages/district_detail.html', context)