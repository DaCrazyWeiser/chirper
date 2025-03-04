from django.contrib import admin
from .models import Chirp, Follow, Profile


@admin.register(Chirp)
class ChirpAdmin(admin.ModelAdmin):
    list_display = ("user", "content", "created_at", "parent", "is_retweet")
    search_fields = ("user__username", "content")
    list_filter = ("created_at", "is_retweet")


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ("follower", "following", "created_at")
    search_fields = ("follower__username", "following__username")
    list_filter = ("created_at",)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "bio")
    search_fields = ("user__username", "bio")
