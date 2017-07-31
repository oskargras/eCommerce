from django.forms import Form, CharField, EmailField, Textarea


class ContactForm(Form):
    name = CharField(required=False, max_length=100, help_text='100 characters max.')
    email = EmailField(required=True)
    comment = CharField(required=True, widget=Textarea)