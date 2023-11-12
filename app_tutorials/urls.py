from django.urls import path

from . import views

urlpatterns = [
    path('tutorials_home_page', views.tutorials_home_page, name="tutorials_home_page"),
]
