from django.shortcuts import render
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.contrib.auth.views import login, logout     
from django.core.urlresolvers import reverse_lazy, reverse
from .forms import CustomUserCreationForm
from .models import MyUser


def home(request):  #Renderiza o template home.html
    return render(request, 'usuarios/home.html')

def login_view(request, *args, **kwargs):   #View para login do usuário
    if request.user.is_authenticated():     #Verifica se o usuário está logado e, se estiver, 
        return HttpResponseRedirect(reverse('usuarios:home'))   #... direciona-o para home.html
    
    kwargs['template_name'] = 'usuarios/login.html'              #Caso o usuário, já logado, tentar acessar a tela de login
    kwargs['extra_context'] = {'next': reverse('usuarios:home')} #... ele será redirecionado para a página de logado.
    return login(request, *args, **kwargs)                    

def logout_view(request, *args, **kwargs):  #View para logout do usuário
    kwargs['next_page'] = reverse('usuarios:home') #Assim que logado, aparece a opção de logout e usuário pode ser redirecionado para home.
    return logout(request, *args, **kwargs)

def search_view(request):   #View para pesquisa de usuários
    email = request.GET.get('email')    #A variável e-mail pega todos os objetos 'email'
    usuarios_por_email = MyUser.objects.filter(email = email)    #usuarios_por_email filtra 
    context = {'usuarios_por_email': usuarios_por_email}
    print (request.POST)
    return render(request, 'usuarios/pesquisar.html', context)    

class RegistrationView(CreateView): #Visualização baseada na classe CreateView
    form_class = CustomUserCreationForm     #Costumiza o form_class para o form de usuarios
    success_url = reverse_lazy('usuarios:login')    #
    template_name = "usuarios/registrar.html"   #Nome do template da página de cadastro.