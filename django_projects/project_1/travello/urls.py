from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path("add", views.add, name="add"),
#     path("add_name", views.add_name, name="add_name")
#
# ]


urlpatterns = [path('', views.index, name="index")]