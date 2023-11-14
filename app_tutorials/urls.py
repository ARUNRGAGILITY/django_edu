from django.urls import path

from . import views

urlpatterns = [
    path('tutorials_home_page', views.tutorials_home_page, name="tutorials_home_page"),
    path('test_markdown', views.test_markdown, name="test_markdown"),
    
    # display_md_topic
    path('display_md_topic/<str:topic>', views.display_md_topic, name="display_md_topic"),
]
