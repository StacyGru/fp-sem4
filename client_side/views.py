from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from .forms import LoginForm
from django.contrib.auth import authenticate, login

from .models import (
    Client, 
    Order, 
    Ride, 
    DiscountCard,
    Operator
)
from driver_side.models import (
    AvailableCar,

)

class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'main.html', {})

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
                if user.is_superuser:
                    return HttpResponseRedirect('/administrator')
                if user.is_staff:
                    return HttpResponseRedirect('/operator')
                return HttpResponseRedirect('/client')                     
        return render(request, 'login.html', {'form': form})



# 3 ТИПА ПОЛЬЗОВАТЕЛЕЙ

class ClientView(View):
    def get(self, request, *args, **kwargs):
        client = Client.objects.get(login = request.user.username) # находим в таблице Клиенты клиента, который авторизовался
        return render(
            request,
            'main.html',
            {'client': client}
        )

class OperatorView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'operator.html',
            {}
        )

class AdministratorView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'administrator.html',
            {}
        )



# ДЛЯ КЛИЕНТА

class ClientOrdersView(View):
    def get(self, request, *args, **kwargs):
        client = Client.objects.get(login = request.user.username) # находим в таблице Клиенты клиента, который авторизовался
        # client_id = client.id
        # client_id - id авторизовавшегося клиента
        orders = Order.objects.filter(client_id=client.id)    
        return render(
            request,
            'client/orders.html',
            {'orders': orders}
        )

class ClientRidesView(View):
    def get(self, request, *args, **kwargs):
        client = Client.objects.get(login = request.user.username) # находим в таблице Клиенты клиента, который авторизовался
        orders = Order.objects.get(client_id=client.id)  # находим в таблице Заказы заказы, у которых client_id = авторизованный_клиент.id
        # for order in orders:
        rides = Ride.objects.filter(order_id=orders.id)
        # rides = Ride.objects.get
        return render(
            request,
            'client/rides.html',
            {'rides': rides}
        )

class ClientDiscountCardView(View):
    def get(self, request, *args, **kwargs):
        client = Client.objects.get(login = request.user.username) # находим в таблице Клиенты клиента, который авторизовался
        discount_card = DiscountCard.objects.get(client_id = client.id)
        return render(
            request,
            'client/discount_card.html',
            {'discount_card': discount_card}
        )



# ДЛЯ ОПЕРАТОРА

class OperatorClientsView(View):
    def get(self, request, *args, **kwargs):
        clients = Client.objects.all()
        return render(
            request,
            'operator/clients.html',
            {'clients': clients}
        )

class OperatorOrdersView(View):
    def get(self, request, *args, **kwargs):
        orders = Order.objects.all()
        return render(
            request,
            'operator/orders.html',
            {'orders': orders}
        )

class OperatorRidesView(View):
    def get(self, request, *args, **kwargs):
        rides = Ride.objects.all()
        return render(
            request,
            'operator/rides.html',
            {'rides': rides}
        )

class OperatorAvailableCarsView(View):
    def get(self, request, *args, **kwargs):
        available_cars = AvailableCar.objects.all()
        return render(
            request,
            'operator/available_cars.html',
            {'available_cars': available_cars}
        )

class OperatorDiscountCardsView(View):
    def get(self, request, *args, **kwargs):
        discount_cards = DiscountCard.objects.all()
        return render(
            request,
            'operator/discount_cards.html',
            {'discount_cards': discount_cards}
        )