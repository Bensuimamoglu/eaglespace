from django.urls import path
from . import views


urlpatterns = [
    path("", views.giris, name="giris"),
    #path("index", views.index, name="home"),
]