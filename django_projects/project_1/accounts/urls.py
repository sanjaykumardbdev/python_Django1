from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path("add", views.add, name="add"),
#     path("add_name", views.add_name, name="add_name")
#
# ]


urlpatterns = [
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
]
