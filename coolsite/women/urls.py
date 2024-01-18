from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('cars/', views.car_mainpage, name='car_list'),
    path('cars/<int:car_id>/', views.car_index, name='car_id'),
    path('client_err_test/', views.err_400),
    path('server_err_test/', views.err_500),
    path('car_sell/', views.car_sell, name='car_sell'),
    path('addpage/', views.addpage, name='addpage'),
    path('posts/', views.create_post, name='posts'),
    path('contact/', views.contact, name='contact'),
]
