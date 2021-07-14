from django.forms.forms import Form
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from django.contrib import messages
from django.db import transaction
from .forms import (
    LoginForm,
    AddClientForm
)
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
    Car,
    ModelDetail,
    Driver,
    Street
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
        orders = Order.objects.filter(client_id=client.id)
        discount_card = DiscountCard.objects.get(client_id = client.id)
        count_orders = orders.count()
        return render(
            request,
            'client.html',
            {
                'client': client,
                'count_orders': count_orders,
                'discount_card': discount_card
            }
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
        form = AddClientForm(request.POST or None)
        return render(
            request,
            'operator/clients.html',
            {
                'clients': clients,
                'form': form
            }
        )
        
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        form = AddClientForm(request.POST or None)
        if form.is_valid():
            new_client = form.save(commit=False)
            new_client.full_name = form.cleaned_data['full_name']
            new_client.phone = form.cleaned_data['phone']
            new_client.gender = form.cleaned_data['gender']
            new_client.login = form.cleaned_data['login']
            new_client.password = form.cleaned_data['password']
            new_client.save()
            messages.add_message(request, messages.INFO, 'Клиент успешно добавлен!')
            return HttpResponseRedirect('/operator/clients')
        messages.add_message(request, messages.ERROR, 'Не удалось добавить клиента!')
        return HttpResponseRedirect('/operator/clients')

    # def delete(self, request, *args, **kwargs):
    #     delete_client = 
    #         messages.add_message(request, messages.INFO, 'Клиент успешно добавлен!')
    #         return HttpResponseRedirect('/operator/clients')
    #     messages.add_message(request, messages.ERROR, 'Не удалось добавить клиента!')
    #     return HttpResponseRedirect('/operator/clients')

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



# ДЛЯ ОПЕРАТОРА

class AdministratorCarsView(View):
    def get(self, request, *args, **kwargs):
        cars = Car.objects.all()
        return render(
            request,
            'administrator/cars.html',
            {'cars': cars}
        )

class AdministratorDriversView(View):
    def get(self, request, *args, **kwargs):
        drivers = Driver.objects.all()
        return render(
            request,
            'administrator/drivers.html',
            {'drivers': drivers}
        )

class AdministratorModelsDetailsView(View):
    def get(self, request, *args, **kwargs):
        models_details = ModelDetail.objects.all()
        return render(
            request,
            'administrator/models_details.html',
            {'models_details': models_details}
        )

class AdministratorStreetsView(View):
    def get(self, request, *args, **kwargs):
        streets = Street.objects.all()
        return render(
            request,
            'administrator/streets.html',
            {'streets': streets}
        )

class AdministratorOperatorsView(View):
    def get(self, request, *args, **kwargs):
        operators = Operator.objects.all()
        return render(
            request,
            'administrator/operators.html',
            {'operators': operators}
        )

# CRUD ДЛЯ ТАБЛИЦЫ КЛИЕНТЫ
def get_client(request, pk):
    client = Client.objects.get(id=pk)
    return render(
            request,
            'operator/clients.html',
            {
                'client': client
            }
        )

def edit_client(request, pk):
    client = Client.objects.get(id=pk)
    form = AddClientForm(instance=client)
    if request.method == 'POST':
        form = AddClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Клиент успешно изменён!')
            return HttpResponseRedirect('/operator/clients')
        messages.add_message(request, messages.ERROR, 'Не удалось изменить клиента!')
    return render(
        request,
        'operator/edit_client.html',
        {
            'client': client,
            'form': form    
        }
    )

def delete_client(request, pk):
    client = Client.objects.get(id=pk)
    if request.method == 'POST':
        client.delete()
        messages.add_message(request, messages.INFO, 'Клиент успешно удалён!')
        return HttpResponseRedirect('/operator/clients')
    return render(
        request,
        'operator/delete_client.html',
        {
            'client': client  
        }
    )