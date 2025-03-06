from django.urls import path
from .views import home, about, search, profile, add_comment, like_chirp


urlpatterns = [
    path('', home, name='home'),
    path('home.html', home, name='home'),
    path('about.html', about, name='about'),
    path('search.html', search, name='search'),
    path('accounts/profile/', profile, name='profile'),
    path("comment/<int:chirp_id>/", add_comment, name="add_comment"),
    path('like/<int:chirp_id>/', like_chirp, name='like_chirp'),


]