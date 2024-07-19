from django.contrib import admin
from .models import FlanPage, FormContact, Flan

# Register your models here.

class FlanPageAdmin(admin.ModelAdmin):
    list_display = ['id','name','images']

class FormContactAdmin(admin.ModelAdmin):
    list_display =['id','name','email','message']

class FlanAdmin(admin.ModelAdmin):
    list_display =['id','name','flanImg']

admin.site.register(FlanPage, FlanPageAdmin)
admin.site.register(FormContact, FormContactAdmin)
admin.site.register(Flan, FlanAdmin)