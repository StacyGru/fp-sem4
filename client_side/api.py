from rest_framework import viewsets, permissions
from .models import Client, Operator, Order, Ride, DiscountCard
from .serializers import ClientSerializer, OperatorSerializer, OrderSerializer, RideSerializer, DiscountCardSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ClientSerializer


class OperatorViewSet(viewsets.ModelViewSet):
    queryset = Operator.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = OperatorSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = OrderSerializer

class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RideSerializer

class DiscountCardViewSet(viewsets.ModelViewSet):
    queryset = DiscountCard.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DiscountCardSerializer