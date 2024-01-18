from django import forms
from .models import *

class addPostForm(forms.Form):
    title = forms.CharField('Название авто', max_length=50)
    type = forms.CharField('Тип авто', max_length=20)
    availability = forms.BooleanField('Наличие')
    range = forms.CharField('Пробег', max_length=20)
    engine = forms.CharField('Тип двигателя', max_length=20)
    date = forms.DateTimeField('Год производства', auto_now_add=True)
    image = forms.ImageField()
    price = forms.CharField('Цена', max_length=20)