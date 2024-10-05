from django.urls import path
from help import views

urlpatterns = [
    path('', views.help, name='help'),

]