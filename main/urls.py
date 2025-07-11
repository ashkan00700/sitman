from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('upload/', views.upload_file, name='upload'),
    path('files/', views.uploaded_files, name='uploaded_files'),
    path('delete/<int:file_id>/', views.delete_file, name='delete_file'),
    path('admin-download/<int:file_id>/', views.download_uploaded_file, name='admin_file_download'),
    path('logout/', views.logout_view, name='logout'),  # custom logout view
]
