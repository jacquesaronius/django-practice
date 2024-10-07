from django.urls import path
from appone.views import index

urlpatterns = [
    path('', index, name="index")
]