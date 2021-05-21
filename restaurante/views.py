from restaurante.forms import RegistrationForm
from django.shortcuts import redirect, render
from django.contrib import messages
from restaurante.models import Pedido
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, forms, login, logout
from datetime import datetime, timedelta
from django.http.response import Http404
from django.db.models import Sum
# Create your views here.


@login_required(login_url='/login/')
def index(request):
    return render(request, 'index.html')


def login_user(request):
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/')


def submit_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)

        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, 'Usuário ou Senha inválido!')

    return redirect('/')


def sucesso(request):
    return render(request, 'sucesso.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages = ('Usuário criado com sucesso!')
            context = {'messages': messages}
            return render(request, 'sucesso.html', context=context)
        else:
            form = RegistrationForm()
            messages = 'Erro: Dados Inválidos!'
            context = {'form': form, 'messages': messages}
            return render(request, 'register.html', context=context)

    else:
        form = RegistrationForm()
        context = {'form': form}
        return render(request, 'register.html', context=context)


@login_required(login_url='/login/')
def pedido(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        proteinas = request.POST.get('proteinas')
        acompanhamentos = request.POST.get('acompanhamentos')
        saladas = request.POST.get('saladas')
        quantidade = request.POST.get('quantidade')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        endereco = request.POST.get('endereco')
        valor = request.POST.get('valor')
        observacao = request.POST.get('observacao')
        data = request.POST.get('data')
        usuario = request.user

        id = request.POST.get('id')
        if id:
            pedidos = Pedido.objects.get(id=id)

            if pedidos.usuario == usuario:
                pedidos.nome = nome
                pedidos.proteinas = proteinas
                pedidos.acompanhamentos = acompanhamentos
                pedidos.saladas = saladas
                pedidos.quantidade = quantidade
                pedidos.email = email
                pedidos.telefone = telefone
                pedidos.endereco = endereco
                pedidos.valor = valor
                pedidos.observacao = observacao
                pedidos.data = data

        else:
            Pedido.objects.create(nome=nome, proteinas=proteinas,
                                  acompanhamentos=acompanhamentos,
                                  saladas=saladas, quantidade=quantidade,
                                  email=email,
                                  telefone=telefone, endereco=endereco,
                                  valor=valor, observacao=observacao,
                                  data=data, usuario=usuario)

    return redirect('/ver_pedido')


@login_required(login_url='/login/')
def ver_pedido(request):
    usuario = request.user
    pedidos = Pedido.objects.filter(usuario=usuario)
    context = {'pedidos': pedidos}
    return render(request, 'pedido.html', context=context)


@login_required(login_url='/login/')
def deletar(request, id):
    usuario = request.user
    try:
        pedido = Pedido.objects.get(id=id)
    except Exception:
        raise Http404()
    if usuario == pedido.usuario:
        pedido.delete()
    else:
        raise Http404()
    return redirect('/ver_pedido')
