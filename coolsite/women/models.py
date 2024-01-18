from django.db import models


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

#class Payment(models.Model):
    #first_name=
    #last_name=
    #email=
    #address=
    #type_payment1= models.BooleanField()
    #type_payment2 = models.BooleanField()
    #type_payment3 = models.BooleanField()
    #card_numb=
    #date_card=
    #cvv=
    #confirm=models.BooleanField()



