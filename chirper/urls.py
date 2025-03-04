from django.urls import path
from .views import home, about, search, profile


urlpatterns = [
    path('', home, name='home'),
    path('home.html', home, name='home'),
    path('about.html', about, name='about'),
    path('search.html', search, name='search'),
    path('accounts/profile/', profile, name='profile'),

]