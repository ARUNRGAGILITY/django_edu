from django.urls import path

from . import views

urlpatterns = [
    path('demo_home_page', views.demo_home_page, name="demo_home_page"),
       
    # display_demo_topic
    path('display_demo_topic/<str:topic>', views.display_demo_topic, name="display_demo_topic"),
]
