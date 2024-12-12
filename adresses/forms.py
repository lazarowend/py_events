from django import forms
from .models import Address


CHOICE_STATE = (
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),
)


class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = [
            'zip_code',
            'state',
            'city',
            'district',
            'road',
            'number',
        ]

    zip_code = forms.CharField(label='CEP', widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'CEPS'}))
    state = forms.ChoiceField(label='Selecione o Estado', choices=CHOICE_STATE, widget=forms.Select(attrs={'class': 'input', 'placeholder': 'Selecione o Estado'}))
    city = forms.CharField(label='Cidade', widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Cidade'}))
    district = forms.CharField(label='Bairro', widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Bairro'}))
    road = forms.CharField(label='Rua', widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Rua'}))
    number = forms.IntegerField(label='Número', widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Número'}))
