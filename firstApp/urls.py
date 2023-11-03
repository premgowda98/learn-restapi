from django.urls import path

from . import views

urlpatterns = [
    path('myapp', views.index),
    path('myapp2', views.index2),
    path('<int:app>', views.handle_all_int),
    path('<str:app>', views.handle_all, name="apps-num"),
    path('', views.root_page)
]

