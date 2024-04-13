# from django.urls import path

# from . import views

# urlpatterns = [
#     path(views.home, name = 'home')
# ]

from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    # Home page
    path('', views.home, name='home'),
    path('shop/products', views.products , name='products'),
   ]

