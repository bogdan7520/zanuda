from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('all_for_home', views.all_for_home_page, name='all_for_home_page'),
    path('Computer_accessories', views.for_comp_page, name='for_comp_page'),
    path('mousepads', views.for_comp_mouse_page, name='for_comp_mouse_page'),
    path('Everything_for_the_kitchen', views.all_for_kitchen_page, name='all_for_kitchen_page'),
    path('beauty_and_health', views.beauty_and_health_page, name='beauty_and_health_page'),
    path('auto_products', views.autotovars_page, name='autotovars_page'),
    path('Everything_for_construction_and_repair', views.all_for_building_page, name='all_for_building_page'),
    path('Bicycle_goods', views.velotovars_page, name='velotovars_page'),
    path('Electronic_accessories', views.electro_a_page, name='electro_a_page'),
    path('B_y_equipment_and_goods', views.b_y_tovars_page, name='b_y_tovars_page'),
    path('remainder', views.ostalnoe_page, name='ostalnoe_page'),
    path('<int:pk>', views.TovarsDetailView.as_view(), name='tovars_details'),
    path('search/', views.SearchResultsView.as_view(), name='search_results')
]