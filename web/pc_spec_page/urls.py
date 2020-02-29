from django.urls import path
from . import views

urlpatterns = [
    path('', views.spec_list, name='spec_list'),
]
