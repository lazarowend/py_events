from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, View
from django.contrib.auth.models import User
from .forms import UserForm
from django.contrib.auth import login, logout


class LoginUserView(View):
    
    
    def get(self, request):
        return render(request, 'login.html')

    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        
        user = User.objects.get(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/events/')

        else:
            print('aqui')
            return render(request, 'login.html', {'error_message': 'Nome de usuário ou senha incorretos.'})

        

class CreateUserView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = UserForm
    success_url = reverse_lazy('list_events')


class LogoutUserView(View):
    
    
    def get(self, request):
        logout(request)
        return redirect('list_events')