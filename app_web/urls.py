from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('about', views.about_page, name="about_page"),
    path('contact_us', views.contact_us_page, name="contact_us_page"),
    
    path('display_web_topic/<str:topic>', views.display_web_topic, name="display_web_topic"),
]
