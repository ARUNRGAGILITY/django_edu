from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # web for web pages: urls
    path('', include('app_web.urls')),
]
