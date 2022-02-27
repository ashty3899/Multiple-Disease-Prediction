from . import views
from django.urls import path

urlpatterns = [
    path('', views.home ),
    path('home', views.home ,name='home'),
    path('diabetes', views.diabetes ,name='diabetes'),
    path('heart', views.heart ,name='heart'),
    path('liver', views.liver ,name='liver')
]