from django.contrib import admin
from . models import *
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class DistrictAdmin(SummernoteModelAdmin):
     summernote_fields = ('description')

class TownshipAdmin(SummernoteModelAdmin):
     summernote_fields = ('description')


admin.site.register(District, DistrictAdmin)
admin.site.register(Township, TownshipAdmin)

