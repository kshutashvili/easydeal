from django.http.request import HttpRequest

from landing.forms import UserContactsForm


def contact_form(HttpRequest):
    return {
        'contact_form': UserContactsForm()
    }