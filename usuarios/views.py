from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User # Importa o modelo User do Django
from django.contrib.messages import constants # Importa constantes de mensagens do Django
from django.contrib import messages # Importa o framework de mensagens do Django
from django.contrib.auth import authenticate
from django.contrib import auth
# Create your views here.
def cadastro(request):
    if request.method == "GET":
     return render(request, 'cadastro.html')
    elif request.method == 'POST':
       username = request.POST.get('username')
       senha = request.POST.get('senha')
       comfirma_senha = request.POST.get('confirma_senha')
       # Aqui você pode adicionar a lógica para salvar o usuário no banco de dados

       if not senha != comfirma_senha:
          messages.add_message(request, constants.ERROR,'As senhas não coincidem.')
          return redirect('/usuarios/cadastro/')
       
       if len(senha) < 6:
          messages.add_message(request, constants.ERROR,'A senha deve ter pelo menos 6 ou mais caracteres.')
          return redirect('/usuarios/cadastro/')

    users = User.objects.filter(username=username)
    if users.exists():
       messages.add_message(request, constants.ERROR,'Já existe um usuário com esse nome.')
       return redirect('/usuarios/cadastro/')
    
    User.objects.create_user(
       username=username,
       password=senha
      )
        
    return redirect('/usuarios/login')
      
def login (request):
    if request.method == "GET":
     return render(request, 'login.html')
    elif request.method =='POST':
      username = request.POST.get('username')
      senha = request.POST.get('senha')

      user = authenticate(request , username=username, password=senha)
      
      if user:
         auth.login(request, user)
         return redirect('/mendorados/')
      
      messages.add_message(request, constants.ERROR,'Usuário ou senha inválidos.')


      return redirect('login')



