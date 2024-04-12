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
    path('', views.products, name='products')

    # Page that shows all the pizzas.
    # path('shop/', views.home, name='home') # Corrected the typo here
]

