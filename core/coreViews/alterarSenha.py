from django.views.generic import View
from django.contrib.auth import update_session_auth_hash
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation
from django.shortcuts import render

from core.validators import password_and_password2_are_equals, current_password_is_valid
import json

class AlterarSenhaView(View):
    
    def get(self, request, *args, **kwargs):
        
        carrinho = []

        if (request.session.get('carrinho')):
            carrinho = json.loads(request.session['carrinho'])
        
        context = {
            'carrinho': carrinho,
            'carrinhoTamanho': len(carrinho),
        }
        
        return render(request, 'core/alterar_senha.html', context)
        
    def post(self, request, *args, **kwargs):
        
        carrinho = []

        if (request.session.get('carrinho')):
            carrinho = json.loads(request.session['carrinho'])
        
        context = {
            'carrinho': carrinho,
            'carrinhoTamanho': len(carrinho),
            'erros': []
        }
        
        senhaAtual = request.POST['senhaAtual']
        
        try:
            current_password_is_valid(senhaAtual, request.user)
        except ValidationError as erros:
            for e in erros:
                context['erros'].append(e)
                
        try:
            password_validation.validate_password(request.POST['senhaNova'])
        except ValidationError as erros:
            for e in erros:
                context['erros'].append(e)
                
        try:
            password_and_password2_are_equals(request.POST['senhaNova'], request.POST['senhaNovaRepetir'])
        except ValidationError as erros:
            for e in erros:
                context['erros'].append(e)
            
        if len(context['erros']) == 0:
            request.user.set_password(request.POST['senhaNova'])
            request.user.save()
            update_session_auth_hash(request, request.user)
            context['sucesso'] = 'Senha alterada com sucesso.'
        
        return render(request, 'core/alterar_senha.html', context)
