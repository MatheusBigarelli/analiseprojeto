from django.shortcuts import render
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from .forms import LoginForm

# Create your views here.

class LoginView(FormView):
    template_name = "login/login.html"
    form_class = LoginForm
    success_url = reverse_lazy('pagina:index')

    def get(self, request):
        error_message = "A página não foi encontrada."
        return render(request, 'login/login.html', {'error_message' : error_message})

    def post(self, request):
        try:
            usuario = request.POST['usuario']
            senha = request.POST['senha']
        except KeyError:
            error_message = "Coloca la"
            return render(request, 'login/login.html', {'error_message' : error_message})

        return render(request, 'login/login.html', {'usuario' : usuario, 'senha' : senha})
