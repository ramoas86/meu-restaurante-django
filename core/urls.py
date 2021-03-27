from django.urls import path

from .coreViews.indexView import IndexView
from .coreViews.cardapioView import CardapioView
from .coreViews.cardapioItemDetalhes import CardapioItemDetalhesView
from .coreViews.carrinho import CarrinhoView
from .coreViews.login import LoginView
from .coreViews.cadastro import CadastroView
from .coreViews.minhaConta import MinhaContaView
from .coreViews.alterarDados import AlterarDadosView
from .coreViews.alterarSenha import AlterarSenhaView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('cardapio', CardapioView.as_view(), name='cardapio'),
    path('item_detalhes', CardapioItemDetalhesView.as_view(), name='item_detalhes'),
    path('carrinho', CarrinhoView.as_view(), name='carrinho'),
    path('login', LoginView.as_view(), name='login'),
    path('cadastro', CadastroView.as_view(), name='cadastro'),
    path('minha_conta', MinhaContaView.as_view(), name='minha_conta'),
    path('alterar_dados', AlterarDadosView.as_view(), name='alterar_dados'),
    path('alterar_senha', AlterarSenhaView.as_view(), name='alterar_senha'),
]
