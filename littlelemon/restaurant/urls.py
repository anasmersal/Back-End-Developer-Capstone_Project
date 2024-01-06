from django.urls import path, include
from .views import *

urlpatterns = [
    path("home/", home, name="home"),
    path("", index),
    path("booking/", bookingview.as_view()),
    path("menu/", menuview.as_view()),
    path("menu/", MenuItemsView.as_view()),
    path("menu/<int:pk>", SingleMenuItemView.as_view()),
]
