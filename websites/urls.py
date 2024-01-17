from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('richmond/', views.richmond, name='richmond'),
    path('kingston/', views.kingston, name='kingston'),
    path('results', views.results, name='results'),
]