from django import forms
from django.forms import ModelForm
from .models import Chirp
from .models import Follow
from .models import Profile


class ChirpForm(ModelForm):
    """Provide a visual chirp component for the user that connects to the database."""

    class Meta:
        model = Chirp
        fields = ["user","content","parent","likes",
                      "is_retweet","original_chirp"]
        
        def clean_chirp(self):
            """Filter out the content of the Caden type's vernacular."""

            content = self.cleaned_chirp["content"]
            forbidden_words = ["sigma","skong","skibidi","brain rot","nebrasketball","amogus"]
            if any(word in content.lower() for word in forbidden_words):
                raise forms.ValidationError("Your chirp contains forbidden words, friend.")
            return content


class Follow(ModelForm):
    """Not sure yet what this needs to look like."""

    class Meta:
        model = Follow
        fields = ["follower", "following"]


class Profile(ModelForm):
    """A small visual profile containing an alterable user, bio, and picture."""

    class Meta:
        model = Profile
        fields = ["user","bio","profile_picture"]