from forms import SelectCurrencyForm

def choose_currency(request):
    initial = {}
    if 'currency' in request.session:
        session_currency = request.session['currency']
        initial={ 'currency': session_currency }

    return {
        'choose_currency_form': SelectCurrencyForm(initial=initial),
    }