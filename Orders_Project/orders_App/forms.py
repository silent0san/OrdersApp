from django.forms import ModelForm
from .models import OrderedDish
from django import forms


class DishForm(ModelForm):

    class Meta:
        model = OrderedDish
        fields = {'name', 'price'}
        widgets = {'created_date': forms.HiddenInput()}

    field_order = ['name', 'price']