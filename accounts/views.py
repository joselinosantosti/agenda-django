from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import FormContato
from contatos.models import Contato
from django.db.models import Count
import json

def login(request):
    if request.method != 'POST':
        return render (request, 'accounts/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('password')

    if not usuario or not senha:
        messages.error(request, 'Erro, campos vazios')

    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        messages.error(request, 'Usuário não existe')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Logado com sucesso')
        return redirect('index')

def logout(request):
    auth.logout(request)
    return redirect('index')

def cadastro(request):
    if request.method != 'POST':
        return render (request, 'accounts/cadastro.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('password')
    senha2 = request.POST.get('password2')

    if not nome or not sobrenome or not email or not usuario or not senha or not senha2:
       messages.error(request, 'Erro, campos vazios')
       return render (request, 'accounts/cadastro.html')
    try:
        validate_email(email)
    except:
        messages.error(request, 'Email inválido')
        return render (request, 'accounts/cadastro.html')

    if len(senha) < 6:
        messages.error(request, 'Senha muito curta')
        return render (request, 'accounts/cadastro.html')

    if senha != senha2:
        messages.error(request, 'Senhas não são iguais')
        return render (request, 'accounts/cadastro.html')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Usuário já existe')
        return render (request, 'accounts/cadastro.html')

    messages.success(request, 'Cadastrado com sucesso. Faça o login')

    user = User.objects.create_user(username=usuario, email=email, password=senha, first_name=nome, last_name=sobrenome)
    user.save()
    return redirect ('login')

@login_required(redirect_field_name='login')
def dashboard(request):

    categorias = Contato.objects.values('categoria')
    print(categorias)
    categorias = json.dumps(['4', 't', '5'])

    return render (request, 'accounts/dashboard.html', {'categorias':categorias})