from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def home(request):
    ctx = {}
    return render(request, 'home.html', ctx)


def about(request):
    ctx = {}
    return render(request, 'about.html', ctx)

@login_required
def userProfile(request):
    user = request.user
    ctx = {"user":user}
    return render(request, 'profile.html', ctx)
