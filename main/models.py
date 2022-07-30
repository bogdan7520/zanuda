from django.db import models
from datetime import date

# Create your models here.
class tovars(models.Model):
    title = models.CharField('Название', max_length=250)
    photo_1 = models.TextField('фото 1', blank=False)
    photo_2 = models.TextField('фото 2', blank=True)
    photo_3 = models.TextField('фото 3', blank=True)
    photo_4 = models.TextField('фото 4', blank=True)
    photo_5 = models.TextField('фото 5', blank=True)
    photo_6 = models.TextField('фото 6', blank=True)
    photo_7 = models.TextField('фото 7', blank=True)
    photo_8 = models.TextField('фото 8', blank=True)
    about = models.TextField('О товаре')
    price = models.CharField('Цена', max_length=20, blank=True)

    on_main = 'На Главную страницу'
    all_for_home = 'Всё для дома'
    computers_a = 'Компьютерные аксессуары'
    for_mouse = 'Коврики для мыши'
    all_for_kitchen = 'Всё для кухни'
    beauty_and_health = 'Красота и здоровье'

    autotovars = 'Автотовары'
    all_for_building = 'Всё для строительства и ремонта'
    velotovars = 'Велотовары'
    electro_a = 'Электронные аксессуары'
    b_y_tovars = 'Б/у техника и товары'
    ostalnoe = 'Остальное'

    choises_tema = [
        (on_main, 'На Главную страницу'),
        (all_for_home, 'Всё для дома'),
        (computers_a, 'Компьютерные аксессуары'),
        (for_mouse, 'Коврики для мыши'),
        (all_for_kitchen, 'Всё для кухни'),
        (beauty_and_health, 'Красота и здоровье'),
        (autotovars, 'Автотовары'),
        (all_for_building, 'Всё для строительства и ремонта'),
        (velotovars, 'Велотовары'),
        (electro_a, 'Электронные аксессуары'),
        (b_y_tovars, 'Б/у техника и товары'),
        (ostalnoe, 'Остальное'),
    ]
    tema = models.CharField(
        'Тема',
        max_length=32,
        choices=choises_tema,
        default=ostalnoe,
    )
    tegs = models.TextField('Теги')
    data = models.DateField('Дата', default=date.today())
    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
    def __str__(self):
        return f'{self.title} | Тема: {self.tema}'











class set_price(models.Model):
    on_price = 'Включить цены'
    of_price = 'Выключить цены'
    choises_price_on_of = [
        (on_price, 'Включить цены'),
        (of_price, 'Выключить цены'),
    ]
    price_on_of = models.CharField(
        'Включить/Выключить цены',
        max_length=14,
        choices=choises_price_on_of,
        default=on_price,
    )
    class Meta:
        verbose_name = 'Включить/Выключить цену'
        verbose_name_plural = 'Включить/Выключить цены'
    def __str__(self):
        if self.price_on_of == 'Включить цены':
            return f'Цены включенны'
        elif self.price_on_of == 'Выключить цены':
            return f'Цены выключенны'