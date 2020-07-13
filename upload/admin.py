from django.contrib import admin

from .models import UploadFile

class UploadFileAdmin(admin.ModelAdmin):
    list_display = ('number', 'comment', 'file')
    list_display_links = ('number', 'file')
    search_fields = ('file',)






admin.site.register(UploadFile, UploadFileAdmin)

