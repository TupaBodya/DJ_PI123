from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, EmailInput, forms

from .models import Post, Contact, Payment


class PaymentForm(ModelForm):
    class Meta:
        model= Payment
        fields= {'first_name','last_name','email','address','type_payment1','type_payment2','type_payment3','card_numb','date_card','cvv','confirm'}
        widgets = {
            "first_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Заголовок:",
            }),
            "last_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Содержимое:",
            }),
            "email": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите свой email:",
            }),
            "address": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите свой email:",
            }),
            "card_numb": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите номер карты:",
            }),
            "date_card": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите срок действия карты:",
            }),
            "cvv": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите CVV код:",
            }),
        }

class UploadFileForm(forms.Form):
    file = forms.FileField(label='Файл')

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'image')

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = {'name', 'phone_number', 'email', 'message'}
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите ваше ФИО:",
            }),
            "phone_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите ваш номер телефона:",
            }),
            "email": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите электронную почту для связи:",
            }),
            "message": Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Содержимое вашего сообщения:",
            }),
        }


class UploadFileForm(forms.Form):
    file = forms.FileField(label='Файл')

