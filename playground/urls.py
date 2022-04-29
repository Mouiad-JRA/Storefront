from django.urls import path
from playground.views import say_hello

# app_name = 'storefront'

urlpatterns = [
    path('hello/', say_hello)

]
