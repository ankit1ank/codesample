from __future__ import unicode_literals

from django.shortcuts import render, redirect
from restaurant.forms import RegistrationForm
from restaurant.models import MenuItem


def home(request):
    menu_items = MenuItem.objects.all()
    args = {'menu_items': menu_items}
    return render(request, 'restaurant/home.html', args)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        form.save()
        return redirect('/')
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'restaurant/register.html', args)
