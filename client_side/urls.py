# from rest_framework import routers
from .api import ClientViewSet, OperatorViewSet, OrderViewSet, RideViewSet, DiscountCardViewSet
from driver_side.api import DriverViewSet, ModelDetailViewSet, CarViewSet, StreetViewSet, AvailableCarViewSet
from .views import(
    LoginView,
    BaseView,
    OrdersView,
    RidesView,
    DiscountCardView
)
from django.urls import path
from django.contrib.auth.views import LogoutView

# router = routers.DefaultRouter()
# router.register('api/clients', ClientViewSet, 'clients')
# router.register('api/operators', OperatorViewSet, 'operators')
# router.register('api/orders', OrderViewSet, 'orders')
# router.register('api/rides', RideViewSet, 'rides')
# router.register('api/discountcards', DiscountCardViewSet, 'discountcards')
# router.register('api/drivers', DriverViewSet, 'drivers')
# router.register('api/modeldetails', ModelDetailViewSet, 'modeldetails')
# router.register('api/cars', CarViewSet, 'cars')
# router.register('api/streets', StreetViewSet, 'streets')
# router.register('api/availablecars', AvailableCarViewSet, 'availablecars')
urlpatterns = [
    # router.urls
    path('', BaseView.as_view(), name='base'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page="/"), name='logout'),
    path('orders/', OrdersView.as_view(), name='orders'),
    path('rides/', RidesView.as_view(), name='rides'),
    path('discount_card/', DiscountCardView.as_view(), name='discount_card')
]