from django.contrib import admin
from apps.countries import models



class PostImageAdmin(admin.TabularInline):
    model = models.CountryImage
    extra = 1


class PostAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    inlines = [PostImageAdmin]

admin.site.register(models.Country, PostAdmin)