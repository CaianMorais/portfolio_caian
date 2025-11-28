from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("localizar_curriculo/", views.localizar_curriculo, name="localizar_curriculo"),
]