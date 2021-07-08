from rest_framework import routers
from .api import ClientViewSet, OperatorViewSet, OrderViewSet, RideViewSet, DiscountCardViewSet
from driver_side.api import DriverViewSet, ModelDetailViewSet, CarViewSet, StreetViewSet, AvailableCarViewSet

router = routers.DefaultRouter()
router.register('api/clients', ClientViewSet, 'clients')
router.register('api/operators', OperatorViewSet, 'operators')
router.register('api/orders', OrderViewSet, 'orders')
router.register('api/rides', RideViewSet, 'rides')
router.register('api/discountcards', DiscountCardViewSet, 'discountcards')
router.register('api/drivers', DriverViewSet, 'drivers')
router.register('api/modeldetails', ModelDetailViewSet, 'modeldetails')
router.register('api/cars', CarViewSet, 'cars')
router.register('api/streets', StreetViewSet, 'streets')
router.register('api/availablecars', AvailableCarViewSet, 'availablecars')
urlpatterns = router.urls