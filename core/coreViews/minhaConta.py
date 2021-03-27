from django.views.generic import View
from django.contrib.auth import logout
from django.shortcuts import render

import json
from core.models import UsuarioInfo

class MinhaContaView(View):
    
    def get(self, request, *args, **kwargs):
        
        carrinho = []

        if (request.session.get('carrinho')):
            carrinho = json.loads(request.session['carrinho'])
        
        context = {
            'carrinho': carrinho,
            'carrinhoTamanho': len(carrinho),
        }
        
        cmd = request.GET.get('cmd')
        
        if (cmd == 'sair'):
            context['sair'] = True
            logout(request)
        else:
            context['usr'] = request.user
            usuarioInfo = UsuarioInfo.objects.get(usuario=request.user)
            context['usrInfo'] = usuarioInfo
            
        return render(request, 'core/minha_conta.html', context)
