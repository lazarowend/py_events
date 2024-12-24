from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, View
from .models import Address
from .forms import AddressForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django_htmx.http import HttpResponseClientRedirect
from django_htmx.http import HttpResponseClientRefresh


@method_decorator(login_required(login_url='login_view'), name='dispatch')
class CreateAddressView(CreateView):
    model = Address
    template_name = 'adresses/create_address.html'
    form_class = AddressForm
    success_url = reverse_lazy('list_user_event_view')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateAddressView(UpdateView):
    model = Address
    template_name = 'adresses/update_address.html'
    context_object_name = 'address'
    form_class = AddressForm
    success_url = reverse_lazy('detail_user_view')


class DeleteAddressView(View):

    def post(self, request, pk):
        if not self.request.user.id == pk:
            return HttpResponseClientRefresh()

        address = Address.objects.get(pk=pk)
        try:
            address.delete()
        except Exception:
            messages.error(self.request, 'Existem Eventos ultilizando este Endereço, Não é possivel apagar.')
            return HttpResponseClientRefresh()

        return HttpResponseClientRedirect(reverse_lazy('detail_user_view'))
