from django.contrib import admin
from .models import Password

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
  list_display = ("id", "data_created", "time", "app_name", "username", "password", "type")
  
admin.site.register(Password, MemberAdmin)
