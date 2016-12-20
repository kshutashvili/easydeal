from landing.forms import UserContactsForm


def contact_form(request):
    return {
        'contact_form': UserContactsForm()
    }