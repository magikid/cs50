from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/new", views.new_entry, name="new_entry"),
    path("wiki/<str:title>", views.get_entry, name="get_entry"),
    path("search", views.get_search_result, name="get_search_result"),
    path("random", views.random_entry, name="random_entry"),
]
