from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pagina/pagina-pessoal.html')

def login(request):
    return render(request, 'pagina/login.html')

def signup(request):
    return render(request, 'pagina/signup.html')
