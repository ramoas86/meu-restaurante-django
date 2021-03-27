from django.db import models
from django.contrib.auth.models import User

from .outros.categoriasCardapio import categoriasCardapio as cat

class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.CharField(max_length=300)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Cardapio(models.Model):

    CATEGORIAS_CARDAPIO = [
        (cat[0], cat[0]),
        (cat[1], cat[1]),
        (cat[2], cat[2]),
        (cat[3], cat[3]),
        (cat[4], cat[4]),
        (cat[5], cat[5]),
    ]

    categoria = models.CharField(
        max_length=30,
        choices=CATEGORIAS_CARDAPIO,
        default=cat[0]
    )
    foto = models.ImageField(upload_to='cardapio')
    nome = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=4, decimal_places=2)
    descricao = models.TextField()

    def __str__(self):
        return self.nome
        
class UsuarioInfo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)
    complemento = models.CharField(max_length=300)
    
    def __str__(self):
        usuarioInfo = f'UsuarioInfo: {self.usuario.username}'
        return usuarioInfo
