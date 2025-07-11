from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, FileResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse
from .forms import FileUploadForm, CustomUserCreationForm
from .models import UploadedFile
from django.contrib.auth import logout
import random

def home(request):
    approved_ads = UploadedFile.objects.filter(is_advertisement=True, is_approved=True)
    ad = random.choice(approved_ads) if approved_ads else None
    return render(request, 'home.html', {'ad': ad})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded = form.save(commit=False)
            uploaded.uploaded_by = request.user
            uploaded.save()
    else:
        form = FileUploadForm()
    return render(request, 'upload.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def uploaded_files(request):
    files = UploadedFile.objects.all().order_by('-uploaded_at')
    return render(request, 'uploaded_files.html', {'files': files})

@staff_member_required
def delete_file(request, file_id):
    file = get_object_or_404(UploadedFile, id=file_id)
    file.file.delete()
    file.delete()
    return HttpResponseRedirect(reverse('uploaded_files'))

@staff_member_required
def download_uploaded_file(request, file_id):
    file = get_object_or_404(UploadedFile, id=file_id)
    return FileResponse(open(file.file.path, 'rb'), as_attachment=True)

def logout_view(request):
    logout(request)
    return redirect('home')
