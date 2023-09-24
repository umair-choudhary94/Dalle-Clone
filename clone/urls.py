
from django.urls import path
from .views import *
urlpatterns = [
    path('',index),
    path('profile/',profile),
    path('login/',login),
    path('signup/',signup),
    path('generate-response/', generate_response, name='generate_response'),
]