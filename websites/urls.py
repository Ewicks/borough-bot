from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('richmond/', views.richmond, name='richmond'),
    path('kingston/', views.kingston, name='kingston'),
    path('elmbridge/', views.elmbridge, name='elmbridge'),
    path('southwark/', views.southwark, name='southwark'),
    path('woking/', views.woking, name='woking'),
    path('results', views.results, name='results'),
]