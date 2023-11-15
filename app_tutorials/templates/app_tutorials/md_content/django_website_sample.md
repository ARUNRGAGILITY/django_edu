<a href="/">Home</a>&nbsp;&nbsp;/&nbsp;&nbsp;<a href="/tutorials/tutorials_home_page">Tutorials Home</a>
<b>Django Website Sample App</b>
<br>
# Django Framework: A simple website with bootstrap template

Creating a simple website with Django, Bootstrap, and a common navbar involves several steps. In this example, I'll guide you through creating a Django project and app, setting up Bootstrap, creating templates, and adding the necessary views and URLs.

**Step 1: Set Up Your Django Project**

If you haven't already, create a new Django project. Let's call it "mywebsite."

```bash
django-admin startproject mywebsite
cd mywebsite
```

**Step 2: Create a Django App**

Create a new Django app within your project. Let's name it "core."

```bash
python manage.py startapp core
```

**Step 3: Define Your Models**

In this example, we won't use any models as the focus is on the website structure. You can add models for products, services, etc., if needed.

**Step 4: Create Templates**

Inside your app's directory, create a "templates" directory if it doesn't exist. Then, create HTML templates for each page:

- Create "home.html," "products.html," "services.html," "about.html," and "contact.html" in the "templates" directory.

Here's an example for "home.html":

```html
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h1>Welcome to My Website</h1>
</body>
</html>
```

Repeat this process for other pages, customizing the content as needed.

**Step 5: Set Up URL Patterns**

In your app's "urls.py" file, define URL patterns for each page:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
```

**Step 6: Create Views**

Define views for each page in your app's "views.py" file. Import the necessary functions and render templates:

```python
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def products(request):
    return render(request, 'products.html')

def services(request):
    return render(request, 'services.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
```

**Step 7: Create a Base Template with Navbar**

In the "templates" directory of your app, create a "base.html" template that includes the common navbar using Bootstrap. Here's an example:

```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Website{% endblock %}</title>
    <!-- Add Bootstrap CSS and other stylesheets here -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet"> 
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="/">My Website</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'home' %}">Home</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'products' %}">Products</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'services' %}">Services</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'about' %}">About</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'contact' %}">Contact Us</a>
                </li>
            </ul>
        </div>
    </nav>
    
    <div class="container">
        {% block content %}
        {% endblock %}
    </div>

    <!-- Add Bootstrap JS and other scripts here -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

**Step 8: Extend Base Template for Each Page**

In your individual HTML templates (e.g., "home.html," "products.html," etc.), extend the "base.html" template and customize the content inside the `{% block content %}` tag. For example, in "home.html":

```html
{% extends 'base.html' %}

{% block title %}Home{% endblock %}

{% block content %}
    <h1>Welcome to My Website</h1>
    <!-- Add home-specific content here -->
{% endblock %}
```

Repeat this process for other pages, replacing the `{% block content %}` content with the respective page content.

**Step 9: Configure URLs**

In the project's "urls.py" (located in "mywebsite" directory), include the app's URL patterns:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]
```

**Step 10: Run the Development Server**

Start the development server:

```bash
python manage.py runserver
```

Now, you can access your website at http://127.0.0.1