from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, View, UpdateView
from django.contrib.auth.models import User
from .forms import UserForm, UpdateUserForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from adresses.models import Address


class LoginUserView(View):

    def get(self, request):
        return render(request, 'users/login.html')

    def post(self, request):
        email = request.POST['email']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(
                request,
                'Usuário não encontrado com esse email.'
            )
            return redirect('/events/login/')

        user = authenticate(request, username=user.username,
                            password=request.POST['password'])
        if user is not None:
            login(request, user)
            messages.success(request, 'Usuário Logado')
            return redirect('/events/')
        else:
            messages.error(request, 'Nome de usuário ou senha incorretos.')
            return render(request, 'login.html')


class CreateUserView(CreateView):
    model = User
    template_name = 'users/register.html'
    form_class = UserForm
    success_url = reverse_lazy('login_user_view')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']

        if User.objects.filter(email=email).exists():
            messages.error(self.request, 'Este email já está em uso.')
            return self.form_invalid(form)

        user = form.save(commit=False)
        user.set_password(password)
        user.save()
        messages.success(self.request, 'Registrado com Sucesso')
        return super().form_valid(form)


class LogoutUserView(View):

    def get(self, request):
        logout(request)
        return redirect('list_event_view')


@method_decorator(login_required(login_url='login_view'), name='dispatch')
class UpdateUserView(UpdateView):
    model = User
    template_name = 'users/update_user.html'
    form_class = UpdateUserForm

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['user'] = User.objects.get(id=self.request.user.id)
        context['adresses'] = Address.objects.filter(user=self.request.user.id)

        return context
    
    def get_success_url(self):
        messages.success(
            self.request,
            'Informações atualizadas com Sucesso'
            )
        return reverse_lazy('update_user_view')
