from django.shortcuts import render, redirect
from .forms import ProfileForm, BusinessForm, PostForm, UpdateForm, ChangeHood
from .models import Profile, Businesses, Neighbour, Feeds
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required


def index(request):
    profile = Profile.objects.filter(user_id=request.user.id)
    title = "Home"
    return render(request, "index.html", {"profile": profile, "title": title})
