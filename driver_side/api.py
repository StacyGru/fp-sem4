from rest_framework import viewsets, permissions
from .models import Driver, ModelDetail, Car, Street, AvailableCar
from .serializers import DriverSerializer, ModelDetailSerializer, CarSerializer, StreetSerializer, AvailableCarSerializer

class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DriverSerializer


class ModelDetailViewSet(viewsets.ModelViewSet):
    queryset = ModelDetail.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ModelDetailSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CarSerializer

class StreetViewSet(viewsets.ModelViewSet):
    queryset = Street.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = StreetSerializer

class AvailableCarViewSet(viewsets.ModelViewSet):
    queryset = AvailableCar.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AvailableCarSerializer