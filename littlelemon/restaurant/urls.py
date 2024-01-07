from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("menu/items/", views.MenuItemsView.as_view(), name="menu-items"),
    path(
        "menu/items/<int:pk>/",
        views.SingleMenuItemView.as_view(),
        name="single-menu-item",
    ),
    path("api-token-auth/", obtain_auth_token),
]
