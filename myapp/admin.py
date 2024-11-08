from django.contrib import admin
from .models import TelevisionShow

class TelevisionShowAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'release_date')
    list_filter = ('genre', 'release_date')  
    search_fields = ('title', 'genre', 'description') 
    ordering = ['release_date']

admin.site.register(TelevisionShow, TelevisionShowAdmin)