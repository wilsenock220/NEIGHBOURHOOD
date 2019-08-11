from .models import Profile, Neighbour, Businesses, Feeds
from django import forms


class ProfileForm(forms.ModelForm):
    class Meta:

        model = Profile
        exclude = ["user"]
        widgets = {"neigbor": forms.Select()}


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Businesses
        exclude = ["user"]
        widgets = {
            "businessesName": forms.TextInput(
                attrs={"placeholder": "Add a business Name"}
            ),
            "email": forms.TextInput(attrs={"placeholder": "Add a business email"}),
        }
