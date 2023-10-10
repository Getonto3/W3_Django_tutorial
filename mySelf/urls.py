from django.urls import path
from . import views

urlpatterns = [
    path('',views.mySelf, name='mySelf'),
    path('details/<int:id>',views.details, name='details'),
]