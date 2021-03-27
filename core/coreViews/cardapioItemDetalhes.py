from django.views.generic import View
from core.models import Cardapio
from django.shortcuts import render
import json

class CardapioItemDetalhesView(View):

    def get(self, request, *args, **kwargs):

        item_adicionado = request.GET.get('item_adicionado')
        id = request.GET.get('id')

        itemCardapio = Cardapio.objects.get(id=id)

        carrinho = []

        if (request.session.get('carrinho')):
            carrinho = json.loads(request.session['carrinho'])

        if item_adicionado != None:

            item = {
                'id': str(itemCardapio.id),
                'nome': str(itemCardapio.nome),
                'fotoUrl': str(itemCardapio.foto.url),
                'valor': str(itemCardapio.valor),
                'descricao': str(itemCardapio.descricao),
            }

            carrinho.append(item)
            carrinhoJSON = json.dumps(carrinho)
            request.session['carrinho'] = carrinhoJSON

        context = {
            'id': id,
            'itemCardapio': itemCardapio,
            'item_adicionado': item_adicionado,
            'carrinhoTamanho': len(carrinho),
        }

        return render(request, 'core/item_detalhes.html', context)
