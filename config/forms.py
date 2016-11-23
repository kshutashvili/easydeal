from django import forms
from .models import SiteConfiguration


class ChoicesForm(forms.ModelForm):
    class Meta:
        model = SiteConfiguration

    def __init__(self, *args, **kwargs):
        super(FooForm, self).__init__(*args, **kwargs)
        current_state = self.instance.state
        ...construct available_choices based on current state...
        self.fields['state'].choices = available_choices
