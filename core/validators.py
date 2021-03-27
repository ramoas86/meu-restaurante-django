from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate
	
def check_user_already_registered(user, email):
	
	userQuery = user.objects.filter(username=email)
	
	if len(userQuery) > 0:
		raise ValidationError(
			_('Usuário já cadastrado.'),
			params={'user': user, 'email': email},
		)
		
def authenticateUserLogin(request):
	
	user = authenticate(username=request.POST['email'], password=request.POST['senha'])
	
	if user == None:
		raise ValidationError(
			_('Usuário ou senha inválido.'),
			params={'request': request},
		)
	else:
		return user
		
def password_and_password2_are_equals(password, password2):
	
	if (password != password2):
		raise ValidationError(
			_('Campos Senha e Repetir Senha não conferem.'),
			params={'password': password, 'password2': password2},
		)
	
def current_password_is_valid(password, user):
	
	if user.check_password(password) == False:
		raise ValidationError(
			_('Senha atual inválida.'),
			params={'password': password, 'user': user},
		)
		
