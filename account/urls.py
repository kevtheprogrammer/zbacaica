 
from django.urls import path
from .views import *

app_name = 'products'

urlpatterns = [
    path('<str:slug>/<int:pk>/', CatDetailView.as_view(),name="category"),
 
]
 