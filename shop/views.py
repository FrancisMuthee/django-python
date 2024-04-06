# from django.shortcuts import render
# from django.http import HttpRequest, HttpResponse

# # Create your views here.
# def home(request):
#     return render(request, 'base.html'), 
#     return render(request, 'index.html'),
#     return HttpResponse(request, index.html)

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # Assuming you want to render 'index.html' as the response
    return render(request, 'base.html')
