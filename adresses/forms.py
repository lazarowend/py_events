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

CHOICE_PUBLIC = (
    (True, 'Público'),
    (False, 'Particular'),
)


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            'place_name',
            'state',
            'city',
            'district',
            'road',
            'number',
            'public'
        ]
    
    
    place_name = forms.CharField(label='Apelido do local', widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Apelido do local'}))
    state = forms.ChoiceField(label='Selecione o Estado', choices=CHOICE_STATE, widget=forms.Select(attrs={'class': 'input', 'placeholder': 'Selecione o Estado'}))
    city = forms.CharField(label='Cidade', widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Cidade'}))
    district = forms.CharField(label='Bairro', widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Bairro'}))
    road = forms.CharField(label='Rua', widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Rua'}))
    number = forms.IntegerField(label='Número', widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Número'}))
    public = forms.ChoiceField(label='Publico: pode ser usado por qualquer pessoa. Privado: só você pode usar', choices=CHOICE_PUBLIC ,widget=forms.Select(attrs={'class': 'input', 'placeholder': ''}))