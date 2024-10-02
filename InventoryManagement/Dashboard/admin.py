from django.contrib import admin
from .models import *

# Register your models here.

admin.site.site_header="Inventory Management System"



class ProductAdmin(admin.ModelAdmin):
    list_display=('name','category','quantity',)
    list_filter=["category"]


admin.site.register(Product,ProductAdmin)
admin.site.register(Order)