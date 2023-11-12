from django.urls import path

from . import views

urlpatterns = [
    path('blog_home_page', views.blog_home_page, name="blog_home_page"),
]
