from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


def contact(request):
    title = 'Contact'
    form = ContactForm(request.POST or None)
    confirm_message = None

    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject = 'Message from MYSITE.com'
        message = '{} {}'.format(comment, name)
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
        title = "Thanks!"
        confirm_message = "Thanks for the message. We will get right back to you."
        form = None

    ctx = {"title": title, "form": form, "confirm_message": confirm_message}
    return render(request, 'contact.html', ctx)
