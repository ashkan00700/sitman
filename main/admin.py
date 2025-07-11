from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import UploadedFile

@admin.register(UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'uploaded_by', 'uploaded_at', 'is_advertisement', 'is_approved', 'download_link')
    list_filter = ('uploaded_by', 'uploaded_at', 'is_advertisement', 'is_approved')
    list_editable = ('is_approved',)
    search_fields = ('file', 'uploaded_by__username')

    def download_link(self, obj):
        url = reverse('admin_file_download', args=[obj.id])
        return format_html('<a href="{}">دانلود فایل</a>', url)
    download_link.short_description = "لینک دانلود"

    def has_module_permission(self, request):
        return request.user.is_superuser

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser