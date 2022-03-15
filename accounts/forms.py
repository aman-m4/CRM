from django.forms import ModelForm
from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model=Order
        fiels='__all__'