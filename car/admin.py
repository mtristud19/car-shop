from django.contrib import admin

from car.models import Car

# Register your models here.

class CarAdmin(admin.ModelAdmin):
    list_display = ['name', 'price','user' ]
    list_filter = ['price']
    search_fields = ['title']
    # inlines = [CommentInline]
admin.site.register(Car, CarAdmin)