from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # web for web pages: urls
    path('', include('app_web.urls')),
    # LoginSystem
    path('loginsys/', include('app_loginsystem.urls')),
    # Courses
    path('courses/', include('app_courses.urls')),
    # Blog
    path('blog/', include('app_blog.urls')),
    # Tutorials
    path('tutorials/', include('app_tutorials.urls')),
    # Transformation
    path('transformation/', include('app_transformation.urls')),
    # Quiz
    path('quiz/', include('app_quiz.urls')),
    # Demo
    path('demo/', include('app_demo.urls')),
    
    
    # markdown
    path('markdownx/', include('markdownx.urls')), 
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)