from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.wiki, name="wiki"),
    path("search/", views.search, name="search"),
    path("new/", views.new, name="new"),
    path("random/", views.random_page, name="random_page"),
    path("wiki/<str:name>/edit/", views.edit, name="edit")
]
