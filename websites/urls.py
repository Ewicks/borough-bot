from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('richmond/', views.richmond, name='richmond'),
    path('kingston/', views.kingston, name='kingston'),
    path('elmbridge/', views.elmbridge, name='elmbridge'),
    path('southwark/', views.southwark, name='southwark'),
    path('guildford/', views.guildford, name='guildford'),
    path('spsom/', views.epsom, name='epsom'),
    path('woking/', views.woking, name='woking'),
    path('lewisham/', views.lewisham, name='lewisham'),
    path('results', views.results, name='results'),
    path('test', views.test, name='test'),
    path('pricing', views.pricing, name='pricing'),
    path('contact', views.contact, name='contact'),
    path('deleteword/<int:pk>/<str:redirect_to>/', views.deleteword, name='deleteword'),
]