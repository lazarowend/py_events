from django import forms
from .models import Event
from adresses.models import Address


CHOICE_TYPE = (
    (1, 'Festa'),
    (2, 'Reunião')
)



class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'name',
            'type_event',
            'description',
            'image',
            'date_event',
            'address',
            'max_tickets',
            'price_ticket'
        ]

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Nome do evento'}))
    type_event = forms.ChoiceField(choices=CHOICE_TYPE, widget=forms.Select(attrs={'class': 'input'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Descrição do evento'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'input', 'placeholder': 'Imagem do evento'}))
    date_event = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'input', 'placeholder': 'YYYY-MM-DD HH:MM', 'type':'datetime-local'}))  # Especificar o formato esperado
    address = forms.ModelChoiceField(queryset=Address.objects.filter(public=True), widget=forms.Select(attrs={'class': 'input'}))
    max_tickets = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input', 'placeholder': 'Limite de ingressos'}))
    price_ticket = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'input', 'placeholder': 'Preço do ingresso'}))
