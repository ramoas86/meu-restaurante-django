from django.views.generic import View
from django.shortcuts import render
import json
from decimal import *

class CarrinhoView(View):

    def get(self, request, *args, **kwargs):

        carrinho = []

        if (request.session.get('carrinho')):
            carrinho = json.loads(request.session['carrinho'])

        id_remover = request.GET.get('id_remover')

        if id_remover != None:
            for itm in carrinho:
                if (itm['id'] == id_remover):
                    carrinho.remove(itm)
                    carrinhoJSON = json.dumps(carrinho)
                    request.session['carrinho'] = carrinhoJSON
                    break

        total = 0

        for itm in carrinho:
            valor = Decimal(itm['valor'])
            total += valor

        context = {
            'carrinho': carrinho,
            'carrinhoTamanho': len(carrinho),
            'total': total,
        }

        return render(request, 'core/carrinho.html', context)
