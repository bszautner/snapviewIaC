from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Photo
from .forms import PhotoForm

def photo_list(request):
    sort = request.GET.get('sort', 'name')
    if sort == 'date':
        photos = Photo.objects.all().order_by('-uploaded_at')
    else:
        photos = Photo.objects.all().order_by('name')
    return render(request, 'album/photo_list.html', {'photos': photos, 'sort': sort})

def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'album/photo_detail.html', {'photo': photo})

@login_required
def photo_upload(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.uploaded_by = request.user
            photo.save()
            messages.success(request, 'Kép sikeresen feltöltve!')
            return redirect('home')
    else:
        form = PhotoForm()
    return render(request, 'album/photo_upload.html', {'form': form})

@login_required
def photo_delete(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    if request.method == 'POST':
        photo.image.delete()
        photo.delete()
        messages.success(request, 'Kép sikeresen törölve!')
        return redirect('home')
    return render(request, 'album/photo_confirm_delete.html', {'photo': photo})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'album/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'album/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')