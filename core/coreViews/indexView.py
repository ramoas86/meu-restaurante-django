from django.views.generic import View
from django.shortcuts import render
from core.models import Noticia
import json

class IndexView(View):

    def get(self, request, *args, **kwargs):
        noticias = Noticia.objects.order_by('-id')

        """
        criar matrix para renderização no template.
        """
        noticiasArray = []
        arrayLinha = []
        indexColeta = 2

        for i in range(len(noticias)):
          if i <= indexColeta:
            arrayLinha.append(noticias[i])
            if i == indexColeta:
              noticiasArray.append(arrayLinha)
              arrayLinha = []
              indexColeta += 3

        if len(arrayLinha) > 0:
          noticiasArray.append(arrayLinha)


        carrinho = []

        if (request.session.get('carrinho')):
            carrinho = json.loads(request.session['carrinho'])

        context = {
            'noticias': noticiasArray,
            'carrinhoTamanho': len(carrinho),
        }

        return render(request, 'core/index.html', context)
