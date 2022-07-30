from django.shortcuts import render
from . models import tovars, set_price
from django.views.generic import DetailView, ListView
from django.db.models import Q

class TovarsDetailView(DetailView):
    model = tovars
    template_name = 'main/detail_view.html'
    context_object_name = 'tovars_on_main_by'
    price_on_of = set_price.objects.all()[0]
    extra_context = {'price_on_of': price_on_of,}


class SearchResultsView(ListView):
    model = tovars
    template_name = 'main/search_results.html'
    price_on_of = set_price.objects.all()[0]
    extra_context = {'price_on_of': price_on_of,}

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = tovars.objects.filter(
            Q(title__icontains=query.lower()) | Q(tegs__icontains=query.lower()) | Q(about__icontains=query.lower())
        )
        return object_list



def home_page(request):
    tovars_on_main = tovars.objects.order_by('-data')[0:10]
    tovars_on_main_by = tovars.objects.all()
    price_on_of = set_price.objects.all()[0]
    dictionary_home = {'tovars_on_main': tovars_on_main, 'tovars_on_main_by': tovars_on_main_by, 'price_on_of': price_on_of}
    return render(request, 'main/home_page.html', dictionary_home)

def all_for_home_page(request):
    tovars_on_main_by = tovars.objects.all()
    price_on_of = set_price.objects.all()[0]
    dictionary_home = {'tovars_on_main_by': tovars_on_main_by, 'price_on_of': price_on_of}
    return render(request, 'main/all_for_home.html', dictionary_home)

def for_comp_page(request):
    tovars_on_main_by = tovars.objects.all()
    price_on_of = set_price.objects.all()[0]
    dictionary_home = {'tovars_on_main_by': tovars_on_main_by, 'price_on_of': price_on_of}
    return render(request, 'main/Computer_accessories.html', dictionary_home)

def for_comp_mouse_page(request):
    tovars_on_main_by = tovars.objects.all()
    price_on_of = set_price.objects.all()[0]
    dictionary_home = {'tovars_on_main_by': tovars_on_main_by, 'price_on_of': price_on_of}
    return render(request, 'main/mousepads.html', dictionary_home)

def all_for_kitchen_page(request):
    tovars_on_main_by = tovars.objects.all()
    price_on_of = set_price.objects.all()[0]
    dictionary_home = {'tovars_on_main_by': tovars_on_main_by, 'price_on_of': price_on_of}
    return render(request, 'main/Everything_for_the_kitchen.html', dictionary_home)

def beauty_and_health_page(request):
    tovars_on_main_by = tovars.objects.all()
    price_on_of = set_price.objects.all()[0]
    dictionary_home = {'tovars_on_main_by': tovars_on_main_by, 'price_on_of': price_on_of}
    return render(request, 'main/beauty_and_health.html', dictionary_home)

def autotovars_page(request):
    tovars_on_main_by = tovars.objects.all()
    price_on_of = set_price.objects.all()[0]
    dictionary_home = {'tovars_on_main_by': tovars_on_main_by, 'price_on_of': price_on_of}
    return render(request, 'main/auto_products.html', dictionary_home)

def all_for_building_page(request):
    tovars_on_main_by = tovars.objects.all()
    price_on_of = set_price.objects.all()[0]
    dictionary_home = {'tovars_on_main_by': tovars_on_main_by, 'price_on_of': price_on_of}
    return render(request, 'main/all_for_construction.html', dictionary_home)

def velotovars_page(request):
    tovars_on_main_by = tovars.objects.all()
    price_on_of = set_price.objects.all()[0]
    dictionary_home = {'tovars_on_main_by': tovars_on_main_by, 'price_on_of': price_on_of}
    return render(request, 'main/Bicycle_goods.html', dictionary_home)

def electro_a_page(request):
    tovars_on_main_by = tovars.objects.all()
    price_on_of = set_price.objects.all()[0]
    dictionary_home = {'tovars_on_main_by': tovars_on_main_by, 'price_on_of': price_on_of}
    return render(request, 'main/Electronic_accessories.html', dictionary_home)

def b_y_tovars_page(request):
    tovars_on_main_by = tovars.objects.all()
    price_on_of = set_price.objects.all()[0]
    dictionary_home = {'tovars_on_main_by': tovars_on_main_by, 'price_on_of': price_on_of}
    return render(request, 'main/B_y_equipment_and_goods.html', dictionary_home)

def ostalnoe_page(request):
    tovars_on_main_by = tovars.objects.all()
    price_on_of = set_price.objects.all()[0]
    dictionary_home = {'tovars_on_main_by': tovars_on_main_by, 'price_on_of': price_on_of}
    return render(request, 'main/remainder.html', dictionary_home)

