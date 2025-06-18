from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cotton/', views.cotton, name='cotton'),
    path('silk/', views.silk, name='silk'),
    path('wool/', views.wool, name='wool'),
    path('linen/', views.linen, name='linen'),
]