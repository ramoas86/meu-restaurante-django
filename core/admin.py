from django.contrib import admin

from .models import Noticia, Cardapio, UsuarioInfo

class NoticiaModelAdmin(admin.ModelAdmin):
    fields = ['titulo', 'texto']

class CardapioModelAdmin(admin.ModelAdmin):
    fields = ['categoria', 'nome', 'valor', 'foto', 'descricao']
    
class UsuarioInfoAdmin(admin.ModelAdmin):
    fields = ['usuario', 'rua', 'numero', 'bairro', 'cep', 'complemento']

admin.site.register(Noticia, NoticiaModelAdmin)
admin.site.register(Cardapio, CardapioModelAdmin)
admin.site.register(UsuarioInfo, UsuarioInfoAdmin)
