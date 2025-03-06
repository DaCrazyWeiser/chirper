from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Chirp, Profile
from chirper import forms

@login_required
def profile_view(request):
    return render(request, 'profile.html', {'user': request.user}),

@login_required
def home(request):
    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            Chirp.objects.create(user=request.user, content=content)
        return redirect("home")  # Redirect to the home page after posting

    chirps = Chirp.objects.all().order_by("-created_at")  # Display recent chirps first
    return render(request, "home.html", {"chirps": chirps})



@login_required  # Ensures only logged-in users can comment
def add_comment(request, chirp_id):
    chirp = get_object_or_404(Chirp, id=chirp_id)  # Get the original chirp

    if request.method == "POST":
        content = request.POST.get("content")  # Get comment text from form
        if content:
            Chirp.objects.create(user=request.user, content=content, parent=chirp)  # Save as reply
    return redirect('home')  # Redirect back to homepage (or chirp detail page)

def like_chirp(request, chirp_id):
    if request.method == 'POST':
        chirp = get_object_or_404(Chirp, id=chirp_id)
        if request.user in chirp.likes.all():
            chirp.likes.remove(request.user)
        else:
            chirp.likes.add(request.user)
        return redirect('home')
    return redirect('home')

def about(request):
    return render(request, 'about.html')  # This renders the about.html template

def search(request):
    return render(request, 'search.html')  # This renders the search.html template

def profile(request):
    form = forms.Profile()
    return render(request, 'profile.html', {"form": form})  # This renders the profile.html template

def chirp_list(request):
    chirps = Chirp.objects.all().order_by('-created_at')  # Get all chirps ordered by created_at
    return render(request, 'chirp_list.html', {'chirps': chirps})