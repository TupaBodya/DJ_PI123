from django.db import models
from django.urls import reverse
import datetime
from django.core.mail import send_mail
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='photos/', default='../../static/women/image/New_post.gif')

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name



class Autoshop(models.Model):
    title = models.CharField('Название авто', max_length=50)
    type = models.CharField('Тип авто', max_length=20)
    availability = models.BooleanField('Наличие')
    range = models.CharField('Пробег', max_length=20)
    engine = models.CharField('Тип двигателя', max_length=20)
    date = models.DateTimeField('Год производства', auto_now_add=True)
    image = models.ImageField()
    price = models.CharField('Цена', max_length=20)

    def __str__(self):
        return self.title


class Payment(models.Model):
    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    email= models.EmailField()
    address= models.CharField(max_length=100)
    type_payment1= models.BooleanField()
    type_payment2 = models.BooleanField()
    type_payment3 = models.BooleanField()
    card_numb= models.CharField(max_length=100)
    date_card= models.CharField(max_length=100)
    cvv= models.CharField(max_length=3)
    confirm=models.BooleanField()

    def __str__(self):
        return self.title



