from django import forms
from apps.polling_units.models import Party


class PartyResultForm(forms.Form):
    party_results = forms.ChoiceField(choices=[], widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        parties = Party.objects.all()  # Retrieve all parties from the database
        choices = [(party.id, party.name) for party in parties]  # Create choices for the party results field
        self.fields['party_results'].choices = choices