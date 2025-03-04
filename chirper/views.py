from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    return render(request, 'profile.html', {'user': request.user}),

def home(request):
    return render(request, 'home.html')  # This renders the home.html template

def about(request):
    return render(request, 'about.html')  # This renders the home.html template

def search(request):
    return render(request, 'search.html')  # This renders the home.html template

def profile(request):
    return render(request, 'profile.html')  # This renders the home.html template
