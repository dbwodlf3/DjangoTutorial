from django.urls import path

from . import views

urlpatterns = [
    path('', views.homeRedirect),
    path('home/', views.home),
]