from django.contrib import admin

from car.models import Car
from car.models import Brand

# Register your models here.

class CarAdmin(admin.ModelAdmin):
    list_display = ['name', 'price','user' ]
    list_filter = ['price']
    search_fields = ['name']
    # inlines = [CommentInline]
admin.site.register(Car, CarAdmin)

class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']
    list_filter = ['country']
    search_fields = ['name']
    # inlines = [CommentInline]
admin.site.register(Brand, BrandAdmin)