from django.contrib.auth.forms import AuthenticationForm
from collections import OrderedDict

from django.urls import reverse_lazy

__author__ = 'user'


def get_menus(request):

    menus = OrderedDict({
        'Home': reverse_lazy('index:index'),
    })
    form_for_login = AuthenticationForm()

    if not request.user.is_authenticated:
        return {'menus': menus, 'form_for_login': form_for_login}
    else:
        menus['My profile'] = reverse_lazy('index:profile')
        menus['LogOut'] = reverse_lazy('index:logout')
        return {'menus': menus}
