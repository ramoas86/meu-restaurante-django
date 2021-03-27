from django.views.generic import View
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import login, password_validation
from django.shortcuts import render, redirect

import json

from core.models import UsuarioInfo
from core.validators import check_user_already_registered, password_and_password2_are_equals

class CadastroView(View):

    def get(self, request, *args, **kwargs):

        carrinho = []

        if (request.session.get('carrinho')):
            carrinho = json.loads(request.session['carrinho'])

        context = {
            'carrinho': carrinho,
            'carrinhoTamanho': len(carrinho),
        }

        return render(request, 'core/cadastro.html', context)

    def post(self, request, *args, **kwargs):
        
        carrinho = []

        if (request.session.get('carrinho')):
            carrinho = json.loads(request.session['carrinho'])
        
        context = {
            'carrinho': carrinho,
            'carrinhoTamanho': len(carrinho),
            'nome': request.POST['nome'],
            'email': request.POST['email'],
            'senha': request.POST['senha'],
            'senha_r': request.POST['senha_r'],
            'erros': [],
        }
        
        try:
            check_user_already_registered(User, context['email'])
        except ValidationError as erros:
            for e in erros:
                context['erros'].append(e)
                
        try:
            password_validation.validate_password(context['senha'])
        except ValidationError as erros:
            for e in erros:
                context['erros'].append(e)
                
        try:
            password_and_password2_are_equals(context['senha'], context['senha_r'])
        except ValidationError as erros:
            for e in erros:
                context['erros'].append(e)
        
        if len(context['erros']) == 0:
            user = User.objects.create_user(context['email'], email=context['email'], password=context['senha'], first_name=context['nome'])
            usuarioInfo = UsuarioInfo(usuario=user)
            usuarioInfo.save()
            login(request, user)
            return redirect('minha_conta')
        else:
            return render(request, 'core/cadastro.html', context)
