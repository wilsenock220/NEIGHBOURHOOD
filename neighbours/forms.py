from .models import Profile, Neighbour, Businesses, Feeds
from django import forms


class ProfileForm(forms.ModelForm):
    class Meta:

        model = Profile
        exclude = ["user"]
        widgets = {"neigbor": forms.Select()}
