from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('<int:month>/', views.months),
    path('<str:name>/', views.detail),
]
