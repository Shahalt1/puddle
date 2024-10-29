from django.urls import path

from . import views

app_name = "conversation"
urlpatterns = [
    path("new/<int:item_pk>", views.new_conversation, name="new_conversation"),
    path("", views.inbox, name="inbox"),
    path("<int:pk>/", views.details, name="details"),
]
