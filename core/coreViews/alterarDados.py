from django.views.generic import View
from django.shortcuts import render, redirect

import json
from core.models import UsuarioInfo

class AlterarDadosView(View):
    
    def get(self, request, *args, **kwargs):
        
        carrinho = []

        if (request.session.get('carrinho')):
            carrinho = json.loads(request.session['carrinho'])
        
        context = {
            'carrinho': carrinho,
            'carrinhoTamanho': len(carrinho),
            'usr': request.user,
            'usrInfo': UsuarioInfo.objects.get(usuario=request.user),
        }
        
        return render(request, 'core/alterar_dados.html', context)
        
    def post(self, request, *args, **kwargs):
        
        request.user.first_name = request.POST['nome']
        
        request.user.save()
        
        usuarioInfo = UsuarioInfo.objects.get(usuario=request.user)
        usuarioInfo.rua = request.POST['rua']
        usuarioInfo.numero = request.POST['numero']
        usuarioInfo.bairro = request.POST['bairro']
        usuarioInfo.cep = request.POST['cep']
        usuarioInfo.complemento = request.POST['complemento']
        
        usuarioInfo.save()
        
        return redirect('minha_conta')
