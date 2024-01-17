from django.core.exceptions import BadRequest
from django.http import HttpResponseNotFound, HttpResponseForbidden, HttpResponseServerError, HttpResponseBadRequest
from django.views.generic.list import ListView
from django.shortcuts import render
from .models import Autoshop


cars = [
    {'id' : 1, 'Model' : 'AUDI A4 B8', "Type" : 'sedan', 'Availability' : True, 'Range' : '209000', 'Engine':'Diesel', 'Date' : '2008', 'Price':'890000₽','image_': 'Audi A4.jpg','image2_': 'Audi A4 2.jpg','image3_': 'Audi A4 3.jpg'},
    {'id' : 2, 'Model' : 'BMW M5 F90', "Type" : 'sedan', 'Availability' : True, 'Range' : '59000', 'Engine':'Gazoline', 'Date' : '2019','Price':'3500000₽','image_': 'BMW M5.jpg','image2_': 'BMW M5 2.jpg','image3_': 'BMW M5 3.jpg'},
    {'id' : 3, 'Model' : 'Mitsubishi Lancer 10 EVO', "Type" : 'sedan', 'Availability' : True, 'Range' : '240300', 'Engine':'Gazoline', 'Date' : '2013','Price':'2000000₽','image_': 'Lancer EVO.jpg','image2_': 'Lancer EVO 2.jpg','image3_': 'Lancer EVO 3.jpg'},
    {'id' : 4, 'Model' : 'Volkswagen Passat B8', "Type" : 'sedan', 'Availability' : False, 'Range' : '13000', 'Engine':'Gazoline','Date' : '2020','Price':'1500000₽','image_': 'VW B8.jpg'},
    {'id' : 5, 'Model' : 'BMW X5', "Type" : 'off-road', 'Availability' : True, 'Range' : '15', 'Engine':'Diesel', 'Date' : '2023','Price':'4500000₽','image_': 'BMW X5.jpg'},
    {'id' : 6, 'Model' : 'Ford Explorer', "Type" : 'off-road', 'Availability' : True, 'Range' : '70000', 'Engine':'Gazoline', 'Date' : '2018','Price':'3500000₽','image_': 'Ford Exp.jpg'}
    ]

menu = [
    {'title': 'Главная страница', 'url_n': 'home'},
    {'title': 'О нас', 'url_n': 'about'},
    {'title': 'Автомобили', 'url_n': 'car_list'},
    {'title': 'Оплатить покупку', 'url_n':'car_sell'}
]


data = {'cars': cars, 'menu': menu, 'car_url': 'car_id'}
def index(request):
    return render(request, 'women/index.html', context=data)
def about(request):
    return render(request, 'women/about.html', context=data)
def apteka(request):
    return render(request, 'women/apteka.html', context=data)

def Base(request):
    autoshop = Autoshop.objects.all()
    return render(request, 'women/Base.html', {'autoshop': autoshop})
def car_index(request, car_id):
    if 1 <= car_id <= 13:
        current = cars[car_id - 1]
        return render(request, 'women/curent_car.html', context=current)


def car_mainpage(request):
    return render(request, 'women/car_list.html', context=data)

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