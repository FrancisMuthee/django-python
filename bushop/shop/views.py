from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'base.html')
    return render(request, 'index.html', {'name': 'El-Franko'})