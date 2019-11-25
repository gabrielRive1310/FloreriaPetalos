#tendra todas las url del sitio web
from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home,name='HOME'),
    path('galeria/',galeria,name='GALE'),

]