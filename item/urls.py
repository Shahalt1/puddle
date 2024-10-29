from django.urls import path
from . import views

app_name = "item"

urlpatterns = [
    path("", views.items, name="items"),
    path("<int:pk>/", views.detail, name="detail"),
    path("new_item/", views.new_item, name="new_item"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/edit/", views.edit_item, name="edit"),
]
