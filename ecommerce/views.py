from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ecommerce_index_view(request):
    '''This function render index page of ecommerce views'''

    return HttpResponse('Welcome to 6410742172 Thitirat Rattanapn views!')

def item_view(request, item_id):
    context_data = {
             "item_id": item_id   
        }
    return render(request, 'index.html',context= context_data)

def homepage_view(request):
    data = {}
    return render(request, 'homepage.html', context = data)

def contacts_view(request):
    data = {}
    return render(request, 'contacts.html', context = data)

def checkout_view(request):
    data = {}
    return render(request, 'checkout.html', context = data)

def products_view(request):
    data = {}
    return render(request, 'products.html', context = data)

def categories_view(request):
    data = {}
    return render(request, 'categories.html', context = data)