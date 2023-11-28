from django.urls import path
from feature import views

urlpatterns = [
    path('', views.index, name='index')
]