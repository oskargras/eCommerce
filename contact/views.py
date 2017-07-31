from django.shortcuts import render


def contact(request):
    ctx = locals()
    return render(request, 'contact.html', ctx)
