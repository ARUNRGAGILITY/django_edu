<a href="/">Home</a>&nbsp;&nbsp;/&nbsp;&nbsp;<a href="/tutorials/tutorials_home_page">Tutorials Home</a>
<b>Django Simple App</b>
<br>
# Django framework: Simple / beginner level - app creation 
Creating a simple Django application involves several steps, including project setup, app creation, defining models, creating views and templates, and running the development server. Here's a step-by-step guide to creating a basic Django application:

**Step 1: Install Django**

If you haven't already, you need to install Django. You can use pip for this:

**High-level Steps**
1. Install Python
2. Install Git
3. Install pipenv
4. Create a Django_projects root folder for all your django work (suggested)
5. Create an Environment for your set of projects or project with prefix env_project1 (suggested)
6. pipenv shell on this folder, to create the virtual env and also once created to go to the virtual env
7. Install django and other django libraries in this virtualenv
8. pip freeze > requirements.txt to save the installation details and restart any future envirornments

```bash
python --version
pip install pipenv
cd <your-root-folder>
mkdir learn_django
cd learn_django
mkdir env_django1
cd env_django1
pipenv shell
<virtual-env>pip install Django
```

**Step 2: Create a Django Project**

Let's create a new Django project called "myproject."

```bash
django-admin startproject myproject .
```

This will create a directory named "myproject" containing the initial project structure.

**Step 3: Navigate to the Project Directory**

Change your current working directory to the project directory:

```bash
cd myproject
```

**Step 4: Create a Django App**

In Django, applications are components within a project. Let's create an app named "myapp":

```bash
python manage.py startapp myapp
```

This command generates a directory named "myapp" containing the app's initial structure.

**Step 5: Define Models**

Open "myapp/models.py" and define your models. For example:

```python
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
```

**Step 6: Create Database Tables**

Run migrations to create database tables based on your models:

```bash
python manage.py makemigrations
python manage.py migrate
```

**Step 7: Create Superuser**

Create a superuser account to access the Django admin interface:

```bash
python manage.py createsuperuser
```

Follow the prompts to set a username, email, and password.

**Step 8: Register Models in Admin**

Open "myapp/admin.py" and register your models:

```python
from django.contrib import admin
from .models import Item

admin.site.register(Item)
```

**Step 9: Create Views**

Create views for your app in "myapp/views.py." Here's an example view:

```python
from django.shortcuts import render
from .models import Item

def item_list(request):
    items = Item.objects.all()
    return render(request, 'myapp/item_list.html', {'items': items})
```

**Step 10: Create Templates**

Create HTML templates for your app in a "templates" directory within your app. For example, create "myapp/templates/myapp/item_list.html" and add your HTML code.

**Step 11: Configure URL Patterns**

Define URL patterns for your app in "myapp/urls.py." For example:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
]
```

**Step 12: Include App URLs in Project URLs**

In "myproject/urls.py," include the app's URL patterns:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]
```

**Step 13: Run the Development Server**

Start the development server:

```bash
python manage.py runserver
```

**Step 14: Access the App**

Visit http://127.0.0.1:8000/ in your web browser to see your app in action. You can access the admin interface at http://127.0.0.1:8000/admin/ using the superuser credentials created earlier.

That's it! You've created a simple Django application with models, views, templates, and URL patterns. You can now build on this foundation to create more complex web applications using Django.