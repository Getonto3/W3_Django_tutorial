from django.contrib import admin
from .models import MySelf

# Register your models here.

class MySelfAdmin(admin.ModelAdmin):
  list_display = ("firstName", "lastName", "nickName","admNo",)

admin.site.register(MySelf, MySelfAdmin)