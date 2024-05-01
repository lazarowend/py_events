from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, View, UpdateView
from django.contrib.auth.models import User
from .forms import UserForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages


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

    def form_valid(self, form):
        if User.objects.filter(username=form.cleaned_data['username']).exists():
            messages.error(self.request, 'Este nome já está em uso.')
            return self.form_invalid(form)
        
        if User.objects.filter(email=form.cleaned_data['email']).exists():
            messages.error(self.request, 'Este email já está em uso.')
            return self.form_invalid(form)

        return super().form_valid(form)



class LogoutUserView(View):
    
    
    def get(self, request):
        logout(request)
        return redirect('list_event_view')


@method_decorator(login_required(login_url='login_view'), name='dispatch')
class UpdateUserView(UpdateView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'user'
    form_class = UserForm
    
    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('profile_view')
