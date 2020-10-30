from django.contrib import admin

# Register your models here.
# from django_projects.project_1.travello.models import Destination
from .models import Destination

admin.site.register(Destination)

