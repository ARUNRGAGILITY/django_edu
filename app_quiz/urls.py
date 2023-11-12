from django.urls import path

from . import views

urlpatterns = [
    path('quiz_home_page', views.quiz_home_page, name="quiz_home_page"),
]
