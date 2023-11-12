1. configured the django
2. configured the runserver


# added markdown
1. markdownx installation 
https://blog.devgenius.io/django-markdown-part-2-installing-an-editor-ff32aadc49d2


use this command from the above blog 
pip install git+https://github.com/neutronX/django-markdownx.git@master

configure the markdownx
INSTALLED_APPS = [    
    ...
    'markdownx', # <-- needed for adding markdown to forms
    ...
]

static files
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media')

urlpatterns = [     
    ...    
    path('markdownx/', include('markdownx.urls')), 
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


models changed
from markdownx.models import MarkdownxField
class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Post(models.Model):
    title = models.CharField(max_length=250)
    content = MarkdownxField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

from markdownx.admin import MarkdownxModelAdmin 
from .models import Post  
admin.site.register(Post, MarkdownxModelAdmin)