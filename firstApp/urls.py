from django.urls import path

from . import views

urlpatterns = [
    path('', views.root_page),
    path('loop', views.loop),
    path('toraise404', views.raise404),
]

