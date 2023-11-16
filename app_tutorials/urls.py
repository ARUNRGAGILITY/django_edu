from django.urls import path

from . import views

urlpatterns = [
    path('tutorials_home_page', views.tutorials_home_page, name="tutorials_home_page"),
    path('test_markdown', views.test_markdown, name="test_markdown"),
    
    # Django Foundation course1
    path('django_course1', views.django_course1, name="django_course1"),
    
    # display_md_topic
    path('display_md_topic/<str:topic>', views.display_md_topic, name="display_md_topic"),
    # display_md_sub_topic
    path('display_md_sub_topic/<str:folder>/<str:topic>', views.display_md_sub_topic, name="display_md_sub_topic"),
]
