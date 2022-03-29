from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name="home"),
    path('hire', views.hire, name="hire"),
]