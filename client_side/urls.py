from .views import (
    MainView,

    LoginView,

    ClientView,
    OperatorView,
    AdministratorView,
    
    ClientOrdersView,
    ClientRidesView,
    ClientDiscountCardView,

    OperatorClientsView,
    OperatorOrdersView,
    OperatorRidesView,
    OperatorAvailableCarsView,
    OperatorDiscountCardsView,

    # AdministratorCarsView,
    # AdministratorDriversView,
    # AdministratorModelsDetailsView,
    # AdministratorStreetsView,
    # AdministratorOperatorsView
)
from django.urls import path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', MainView.as_view(), name='main'), # главная страница: отображается только если никто не авторизован

    path('login/', LoginView.as_view(), name='login'), # страница авторизации (общая для всех 3-х типов пользователей)
    path('logout/', LogoutView.as_view(next_page="/"), name='logout'), # выход

    path('client/', ClientView.as_view(), name='client'), # профиль клиента (дашбоард)
    path('operator/', OperatorView.as_view(), name='operator'), # профиль оператора (дашбоард)
    path('administrator/', AdministratorView.as_view(), name='administrator'), # профиль администратора (дашбоард)

    path('client/orders/', ClientOrdersView.as_view(), name='client/orders'),
    path('client/rides/', ClientRidesView.as_view(), name='client/rides'), # (этого не будет, это будет отобр. в заказах через join)
    path('client/discount_card/', ClientDiscountCardView.as_view(), name='client/discount_card'), # (этого тоже не будет - отобр. строкой в дашбоарде)

    path('operator/clients/', OperatorClientsView.as_view(), name='operator/clients'),
    path('operator/orders/', OperatorOrdersView.as_view(), name='operator/orders'),
    path('operator/rides/', OperatorRidesView.as_view(), name='operator/rides'),
    path('operator/available_cars/', OperatorAvailableCarsView.as_view(), name='operator/available_cars'),
    path('operator/discount_cards/', OperatorDiscountCardsView.as_view(), name='operator/discount_cards'),

    # path('administrator/cars/', AdministratorCarsView.as_view(), name='administrator/cars'),
    # path('administrator/drivers/', AdministratorDriversView.as_view(), name='administrator/drivers'),
    # path('administrator/models_details/', AdministratorModelsDetailsView.as_view(), name='administrator/models_details'),
    # path('administrator/streets/', AdministratorStreetsView.as_view(), name='administrator/streets'),
    # path('administrator/operators/', AdministratorOperatorsView.as_view(), name='administrator/operators'),
]