from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from chirper import forms

@login_required
def profile_view(request):
    return render(request, 'profile.html', {'user': request.user}),

# Saves the chirp if it is entered as a POST request; empty forms are returned as a GET.
def home(request):
    if request.method == "POST":
        form = forms.ChirpForm(request.POST)
        if form.is_valid():
            chirp = form.save(commit=False) # Don't save it yet
            chirp.user = request.user       # Assign the logged in user
            chirp.save()
            return redirect("home")

    else:
        form = forms.ChirpForm()

        return render(request, 'home.html', {"form": form})  # This renders the home.html template


def about(request):
    return render(request, 'about.html')  # This renders the about.html template

def search(request):
    return render(request, 'search.html')  # This renders the search.html template

def profile(request):
    form = forms.Profile()
    return render(request, 'profile.html', {"form": form})  # This renders the profile.html template
