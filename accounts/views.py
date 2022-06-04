from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from . models import FormRemedio, Remedio


def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        messages.error(request, 'Usuário ou senha inválidos!')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Login efetuado com sucesso.')
        return redirect('dashboard')


def logout(request):
    auth.logout(request)
    return redirect('index')


def cadastro(request):
    if request.method != 'POST':
        return render(request, 'accounts/cadastro.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not nome or not sobrenome or not email or not usuario or not senha or not senha2:
        messages.error(request, 'Nenhum campo pode estar vazio!')
        return render(request, 'accounts/cadastro.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'E-mail inválido!')
        return render(request, 'accounts/cadastro.html')

    if len(senha) < 6:
        messages.error(request, 'A senha deve conter pelo menos 6 caracteres!')
        return render(request, 'accounts/cadastro.html')

    if len(usuario) < 8:
        messages.error(request, 'O usuário deve conter pelo menos 8 caracteres!')
        return render(request, 'accounts/cadastro.html')

    if senha != senha2:
        messages.error(request, 'As senhas devem ser iguais!')
        return render(request, 'accounts/cadastro.html')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Usuário já existe na base de dados.')
        return render(request, 'accounts/cadastro.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'E-mail já cadastrado.')
        return render(request, 'accounts/cadastro.html')

    messages.success(request, 'Cadastro efetuado com sucesso!')

    user = User.objects.create_user(username=usuario, email=email, password=senha,
                                    first_name=nome, last_name=sobrenome)
    user.save()
    return redirect('login')


@login_required(redirect_field_name='login')
def dashboard(request):
    if request.method != 'POST':
        form = FormRemedio()
        return render(request, 'accounts/dashboard.html', {'form': form})

    form = FormRemedio(request.POST, request.FILES)

    if not form.is_valid():
        messages.error(request, 'Erro ao enviar o formulário!')

        form = FormRemedio(request.POST)
        return render(request, 'accounts/dashboard.html', {'form': form})

    descricao = request.POST.get('descricao')

    if len(descricao) < 10:
        messages.error(request, 'O campo descrição deve conter pelo menos 10 caracteres.')
        form = FormRemedio(request.POST)
        return render(request, 'accounts/dashboard.html', {'form': form})

    form.save()
    messages.success(request, f'Medicamento {request.POST.get("nome")} salvo com sucesso.')

    return redirect('dashboard')


