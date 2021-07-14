from django import forms
from django.contrib.auth.models import User
from django.forms import widgets
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

class LoginForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'Пользователь с логином {username} не найден в системе!')
        user = User.objects.filter(username=username).first()
        if user:
            if not user.check_password(password):
                raise forms.ValidationError('Неверный пароль!')
        return self.cleaned_data
    
    class Meta:
        model = User
        fields = ['username', 'password']
        help_texts = {
            'username': None,
        }

class AddClientForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput)
    phone = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full_name'].label = 'ФИО'
        self.fields['phone'].label = 'Телефон'
        self.fields['gender'].label = 'Пол'
        self.fields['login'].label = 'Логин'
        self.fields['password'].label = 'Пароль'
    
    class Meta:
        model = Client
        fields = ['full_name', 'phone', 'gender', 'login', 'password']