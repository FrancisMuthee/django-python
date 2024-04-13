# from django.shortcuts import render
# from django.http import HttpRequest, HttpResponse

# # Create your views here.
# def home(request):
#     return render(request, 'base.html'), 
#     return render(request, 'index.html'),
#     return HttpResponse(request, index.html)

from django.shortcuts import render
from django.http import HttpResponse
from .models import items

# Create your views here.
def home(request):
    # Assuming you want to render 'index.html' as the response
    return render(request, 'base.html')

def products(request):

    item1 = items()
    item1.price = 'Ksh. 700'
    item1.name = 'Latte'
    item1.img = 'cup.jpeg'
    item1.desc = 'I want some latted coffee'

    item2 = items()
    item2.price = 'Ksh. 150'
    item2.name = 'Latte'
    item2.img = 'cnn.jpg'
    item2.desc = 'As black as...'

    item3 = items()
    item3.price = 'Ksh. 999'
    item3.name = 'Latte'
    item3.img = 'Arabica.jpg'
    item3.desc = 'From farm to cup'

    item4 = items()
    item4.price = 'Ksh. 999'
    item4.name = 'Latte'
    item4.img = 'Arabica.jpg'
    item4.desc = 'From farm to cup'

    itemss = [item1, item2, item3, item4]

    return render(request, 'products.html', {'itemss': itemss})

def testimonials(request):
    return render(request, 'testimonials.html')

def contact(request):
    return render(request, 'contact.html')
