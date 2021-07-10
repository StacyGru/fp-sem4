from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from .models import Client, Order

# Create your views here.

class BaseView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'base.html', {})

class LoginView(View):

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        context = {'form': form}
        return render(request, 'login.html', context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('/profile')
        return render(request, 'login.html', {'form': form})

class ProfileView(View):
    def get(self, request, *args, **kwargs):
        client = Client.objects.get(pk = request.user.pk)
        orders = Order.objects.filter(client=client)
        return render(
            request,
            'profile.html',
            {'orders': orders}
        )