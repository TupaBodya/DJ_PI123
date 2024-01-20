from django.core.exceptions import BadRequest
from django.http import HttpResponseNotFound, HttpResponseForbidden, HttpResponseServerError, HttpResponseBadRequest
from django.views.generic.list import ListView
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *


cars = [
    {'id' : 1, 'Model' : 'AUDI A4 B8', "Type" : 'sedan', 'Availability' : True, 'Range' : '209000', 'Engine':'Diesel', 'Date' : '2008', 'Price':'890000₽','image_': 'Audi A4.jpg','image2_': 'Audi A4 2.jpg','image3_': 'Audi A4 3.jpg'},
    {'id' : 2, 'Model' : 'BMW M5 F90', "Type" : 'sedan', 'Availability' : True, 'Range' : '59000', 'Engine':'Gazoline', 'Date' : '2019','Price':'3500000₽','image_': 'BMW M5.jpg','image2_': 'BMW M5 2.jpg','image3_': 'BMW M5 3.jpg'},
    {'id' : 3, 'Model' : 'Mitsubishi Lancer 10 EVO', "Type" : 'sedan', 'Availability' : True, 'Range' : '240300', 'Engine':'Gazoline', 'Date' : '2013','Price':'2000000₽','image_': 'Lancer EVO.jpg','image2_': 'Lancer EVO 2.jpg','image3_': 'Lancer EVO 3.jpg'},
    {'id' : 4, 'Model' : 'Volkswagen Passat B8', "Type" : 'sedan', 'Availability' : False, 'Range' : '13000', 'Engine':'Diesel','Date' : '2020','Price':'1500000₽','image_': 'VW B8.jpg','image2_': 'VW B8 2.jpg','image3_': 'VW B8 3.jpg'},
    {'id' : 5, 'Model' : 'BMW X5', "Type" : 'off-road', 'Availability' : True, 'Range' : '15', 'Engine':'Diesel', 'Date' : '2023','Price':'4500000₽','image_': 'BMW X5.jpg', 'image2_': 'BMW X5 2.jpg','image3_': 'BMW X5 3.jpg'},
    {'id' : 6, 'Model' : 'Ford Explorer', "Type" : 'off-road', 'Availability' : True, 'Range' : '70000', 'Engine':'Gazoline', 'Date' : '2018','Price':'3500000₽','image_': 'Ford Exp.jpg', 'image2_': 'Ford 2.jpeg','image3_': 'Ford 3.jpg'},
    {'id' : 7, 'Model' : 'Chevrolet Tahoe', "Type" : 'off-road', 'Availability' : False, 'Range' : '35321', 'Engine':'Diesel', 'Date' : '2018','Price':'7000000₽','image_': 'Chev 1.jpeg', 'image2_': 'Chev 2.jpg','image3_': 'Chev 3.jpg'}
    ]

menu = [
    {'title': 'Главная страница', 'url_n': 'home'},
    {'title': 'О нас', 'url_n': 'about'},
    {'title': 'Автомобили', 'url_n': 'car_list'},
    {'title': 'Оплатить покупку', 'url_n':'addpage'},
    {'title': 'Опубликовать статью', 'url_n':'posts'}
]


data = {'cars': cars, 'menu': menu, 'car_url': 'car_id'}

def index(request):
    return render(request, 'women/index.html', context=data)

def addpage(request):
    return render(request, 'women/addpage.html', context=data)

def Base(request):
    autoshop = Autoshop.objects.all()
    return render(request, 'women/Base.html', {'autoshop': autoshop})
def car_index(request, car_id):
    if 1 <= car_id <= 13:
        current = cars[car_id - 1]
        return render(request, 'women/curent_car.html', context=current)



def contact(request) :
    error = ''
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
    form = ContactForm()
    data = {
        'title': 'Связь со мной',
        'form': form,
        'error': error,
    }
    return render(request, 'women/contact.html',  data)

def payment(request) :
    error = ''
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Форма была неверной'
    form = ContactForm()
    data = {
        'title': 'Связь со мной',
        'form': form,
        'error': error,
    }
    return render(request, 'women/car_sell.html',  data)



def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'women/posts.html', {'form': form})
def about(request):
    posts = Post.objects.all()
    return render(request, 'women/about.html', {'posts': posts})


def create_car_list(request):
    if request.method == 'POST':
        form = AutoshopForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('home')
    else:
        form = AutoshopForm()
    return render(request, 'women/add_car.html', {'form': form})

def car_mainpage(request):
    vehicles = Autoshop.objects.all()
    return render(request, 'women/car_list.html', {'vehicles': vehicles})

def car_sell(request):
    return render(request, 'women/car_sell.html', context=data)

def curent_car(request,car_id):
    return render(request, 'women/curent_car.html', context=data)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
def Forbidden(request, exception):
    return HttpResponseForbidden('<h1>Доступ запрещён</h1>')
def InternalServerError(request):
    return HttpResponseServerError('<h1>Ошибка сервера</h1>')
def ErrBadRequest(request, exception):
    return HttpResponseBadRequest('<h1>Неверный запрос</h1>')
def err_400(request):
    raise BadRequest
def err_500(request):
    raise
# имитация ошибки сервера