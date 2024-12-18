from django.db import models
from django.contrib.auth.models import User


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


class Address(models.Model):
    zip_code = models.CharField(max_length=8)
    state = models.CharField(max_length=2, choices=CHOICE_STATE)
    city = models.CharField(max_length=150)
    district = models.CharField(max_length=100)
    road = models.CharField(max_length=100)
    number = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='address_user')
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return f'{self.name} - {self.road} {self.number} - {self.district}, {self.city} - {self.state}'
