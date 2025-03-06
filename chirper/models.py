from django.db import models
from django.contrib.auth.models import User


class Chirp(models.Model):
    """
    Represents a chirp (a short message similar to a tweet).

    Attributes:
        user (ForeignKey): The user who created the chirp.
        content (CharField): The content of the chirp, limited to 255 characters.
        created_at (DateTimeField): Timestamp of when the chirp was created.
        parent (ForeignKey): Optional field; if set, this chirp is a reply to another chirp.
        likes (ManyToManyField): Users who liked the chirp.
        is_retweet (BooleanField): Indicates if the chirp is a retweet.
        original_chirp (ForeignKey): References the original chirp if this is a retweet.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chirps")
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.CASCADE, related_name="replies"
    )
    likes = models.ManyToManyField(User, blank=True, related_name="liked_chirps")
    is_retweet = models.BooleanField(default=False)
    original_chirp = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="retweets",
    )

    def __str__(self):
        """
        Returns a string representation of the chirp.
        """
        return f"{self.user.username}: {self.content[:50]}"

    def like_count(self):
        return self.likes.count()  # Returns total likes

class Follow(models.Model):
    """
    Tracks following relationships between users.

    Attributes:
        follower (ForeignKey): The user who follows another user.
        following (ForeignKey): The user being followed.
        created_at (DateTimeField): Timestamp of when the follow relationship was created.

    Meta:
        unique_together: Ensures that a user cannot follow the same person more than once.
    """

    follower = models.ForeignKey(
        User, related_name="following", on_delete=models.CASCADE
    )
    following = models.ForeignKey(
        User, related_name="followers", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("follower", "following")

    def __str__(self):
        """
        Returns a string representation of the follow relationship.
        """
        return f"{self.follower.username} follows {self.following.username}"


class Profile(models.Model):
    """
    Provides additional user profile information.

    Attributes:
        user (OneToOneField): The associated user.
        bio (TextField): A brief biography of the user.
        profile_picture (ImageField): An optional profile picture of the user.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to="profiles/", blank=True, null=True)

    def __str__(self):
        """
        Returns a string representation of the user's profile.
        """
        return f"{self.user.username}'s Profile"
