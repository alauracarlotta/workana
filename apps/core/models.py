from datetime import datetime
from django.db import models

## Cadastro de clientes
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    telefone = models.CharField(max_length=15)
    
    def __str__(self):
        return "{} - {}".format(self.name, self.email)
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['-id']

# Tipo de Imóvel
class ImmobileType(models.TextChoices):
    APARTAMENT = 'APARTAMENTO', 'APARTAMENTO'
    KITNET = 'KITNET', 'KITNET'
    HOUSE = 'HOUSE', 'HOUSE'

# Imóvel
class Immobile(models.Model):
    code = models.CharField(max_length=100)
    type_item = models.CharField(max_length=100, choices=ImmobileType.choices)
    address = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_locate = models.BooleanField(default=False)
    
    def __str__(self):
        return "{} - {}".format(self.code, self.type_item)
    
    class Meta:
        verbose_name = 'Imóvel'
        verbose_name_plural = 'Imóveis'
        ordering = ['-id']

# Cadastrar Imagens do Imóvel
class ImmobileImages(models.Model):
    image = models.ImageField('Images', upload_to='imgs')
    immobile = models.ForeignKey(Immobile, related_name='immobile_images', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.immobile.code

# Registrar Locação
class RegisterLocation(models.Model):
    immobile = models.ForeignKey(Immobile, on_delete=models.CASCADE, related_name='register_location')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_start = models.DateTimeField('Início')
    date_end = models.DateTimeField('Fim')
    create_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return "{} - {}".format(self.client, self.immobile)
    
    class Meta:
        verbose_name = 'Registrar Locação'
        verbose_name_plural = 'Registrar Locação'
        ordering = ['-id']
