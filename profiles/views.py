from django.shortcuts import render


# Create your views here.


def home(request):
    ctx = locals()
    return render(request, 'home.html', ctx)


def about(request):
    ctx = locals()
    return render(request, 'about.html', ctx)
