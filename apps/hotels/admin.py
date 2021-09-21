from django.contrib import admin
from apps.hotels import models


# Register your models here.
class HotelImageAdmin(admin.TabularInline):
    model = models.HotelImage
    extra = 1

class HotelAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    inlines = [HotelImageAdmin]

admin.site.register(models.Hotel, HotelAdmin)
admin.site.register(models.Like)