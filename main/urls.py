from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('orgName', views.index, name='orgName'),
    path('inn', views.inn, name='inn'),
    path('corner', views.corner, name='corner'),
    path('reviews', views.reviews, name='reviews'),
    path('other', views.other, name='other'),
    path('auth', views.auth, name='auth'),
    path('register', views.reg, name='register')
]
