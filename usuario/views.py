from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email

# Create your views here.
def login(request):
    
    if request.method != 'POST':
        
        return render(request, 'usuario/login.html')
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    user = auth.authenticate(request, username=username, password=password)
    if not user:
        messages.error(request, 'Usuário ou senha inválidos')
        return render(request, 'usuario/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Você fez login com sucesso!')
        return redirect('orcamento')

def logout(request):
    auth.logout(request)
    return redirect('login')


def cadastro(request):
    if request.user.is_authenticated:
        return redirect('orcamento')
    if request.method != 'POST':
        return render(request, 'usuario/cadastro.html')

    name = request.POST.get('name')
    username = request.POST.get('username')
    email = request.POST.get('email')
    tel = request.POST.get('tel')
    password = request.POST.get('password')
    password2 = request.POST.get('password2')
    if not name or not email or not username or not password or not password2:
        messages.error(request, 'Nenhum campo pode estar vazio')
        return render(request, 'usuario/cadastro.html')
    try:
        validate_email(email)
    except:
        messages.error(request, 'Email inválido.')
        return render(request, 'usuario/cadastro.html')


    if len(password) < 5:
        messages.error(request, 'Senha precisa ter 6 caracteres ou mais.')
        return render(request, 'usuario/cadastro.html')

    if len(username) < 5:
        messages.error(request, 'Usuário precisa ter 6 caracteres ou mais.')
        return render(request, 'usuario/cadastro.html')

    if password2 != password:
        messages.error(request, 'Senhas nao conferem.')
        return render(request, 'usuario/cadastro.html')

    if User.objects.filter(username=username).exists():
        messages.error(request, 'Usuário já cadastrado!')
        return render(request, 'usuario/cadastro.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'Este email já está cadastrado')
        return render(request, 'usuario/cadastro.html')

    messages.success(request, 'Cadastro efetuado com sucesso!')
    if username == 'admin':
        user = User.objects.create_superuser(username=username, email=email, password=password, first_name=name)
        return render(request, 'usuario/cadastro.html')
    user = User.objects.create_user(username=username, email=email, password=password, first_name=name, tel=tel)
    user.save()

    return redirect('login')


@login_required
def orcamento(request):
    return render(request, 'usuario/orcamento.html')