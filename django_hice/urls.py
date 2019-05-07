from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ajax/run/', views.run, name='run'),
    path('ajax/result/', views.result, name='result',),
]
