from django import forms
from .models import Event
from adresses.models import Address


CHOICE_TYPE = (
    (1, 'Festa'),
    (2, 'Reunião')
)


class EventForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['address'].queryset = Address.objects.filter(user=user)


    class Meta:
        model = Event
        fields = [
            'name',
            'type_event',
            'description',
            'date_event',
            'address',
        ]

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Nome do evento'}))
    type_event = forms.ChoiceField(choices=CHOICE_TYPE, widget=forms.Select(attrs={'class': 'input'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Descrição do evento'}))
    date_event = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'input', 'placeholder': 'YYYY-MM-DD HH:MM', 'type':'datetime-local'}))  # Especificar o formato esperado
    address = forms.ModelChoiceField(
        queryset=Address.objects.none(), widget=forms.Select(attrs={'class': 'input'}))
