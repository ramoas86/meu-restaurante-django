from django.views.generic import View
from core.models import Cardapio
from django.shortcuts import render
from core.outros.categoriasCardapio import categoriasCardapio
import json

class CardapioView(View):

    def get(self, request, *args, **kwargs):

        categoria = request.GET.get('categoria')
        item_adicionado = request.GET.get('item_adicionado')
        id = request.GET.get('id')

        carrinho = []

        if (request.session.get('carrinho')):
            carrinho = json.loads(request.session['carrinho'])

        if categoria == None:
            context = {
                'categoriasCardapio': categoriasCardapio,
                'carrinhoTamanho': len(carrinho),
            }

            return render(request, 'core/cardapio.html', context)
        else:

            pratosQuery = Cardapio.objects.filter(categoria=categoria)

            """
            criar matrix para renderização no template.
            """

            cardapioCatArray = []
            arrayLinha = []
            indexColeta = 2

            for i in range(len(pratosQuery)):
              if i <= indexColeta:
                arrayLinha.append(pratosQuery[i])
                if i == indexColeta:
                  cardapioCatArray.push(arrayLinha)
                  arrayLinha = []
                  indexColeta += 3

            if len(arrayLinha) > 0:
              cardapioCatArray.append(arrayLinha)

            if item_adicionado != None:

                itemCardapio = Cardapio.objects.get(id=id)

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
                'categoria': categoria,
                'pratos': cardapioCatArray,
                'item_adicionado': item_adicionado,
                'carrinhoTamanho': len(carrinho),
            }

            return render(request, 'core/cardapio.html', context)