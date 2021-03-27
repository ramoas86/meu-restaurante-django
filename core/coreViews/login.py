from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

import json

from core.validators import authenticateUserLogin

class LoginView(View):

    def get(self, request, *args, **kwargs):

        carrinho = []

        if (request.session.get('carrinho')):
            carrinho = json.loads(request.session['carrinho'])

        context = {
            'carrinho': carrinho,
            'carrinhoTamanho': len(carrinho),
        }

        return render(request, 'core/login.html', context)
        
    def post(self, request, *args, **kwargs):
        
        carrinho = []

        if (request.session.get('carrinho')):
            carrinho = json.loads(request.session['carrinho'])
        
        context = {
            'carrinho': carrinho,
            'carrinhoTamanho': len(carrinho),
            'email': request.POST['email'],
            'senha': request.POST['senha'],
            'erros': [],
        }
            
        try:
            user = authenticateUserLogin(request)
        except ValidationError as erros:
            for e in erros:
                context['erros'].append(e)
            
        if len(context['erros']) == 0:
            login(request, user)
            return redirect('minha_conta')
        else:
             return render(request, 'core/login.html', context)
