from django.urls import path

from . import views

urlpatterns = [
    path('courses_home_page', views.courses_home_page, name="courses_home_page"),
]
