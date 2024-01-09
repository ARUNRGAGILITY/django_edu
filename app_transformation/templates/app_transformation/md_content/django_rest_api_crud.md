<a href="/">Home</a>&nbsp;&nbsp;/&nbsp;&nbsp;<a href="/tutorials/tutorials_home_page">Tutorials Home</a>
<b> Django REST API Framework CRUD Example</b>
<br>
# Django REST API Framework CRUD Example
Let's create a simple Django REST API project for managing a list of tasks (To-Do items) using function-based views. You'll be able to add, modify, and expose these tasks through API endpoints.

**Step 1: Create a New Django Project**

If you haven't already, create a new Django project as described in the previous response.

**Step 2: Create a Django App**

Inside your project directory, create a new Django app named `todo`:

```bash
python manage.py startapp todo
```

**Step 3: Define Your Model**

In your `todo` app, define a model for the tasks in the `models.py` file:

```python
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
```

**Step 4: Create Serializers**

Create a serializer for the `Task` model in your `todo` app's `serializers.py` file:

```python
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
```

**Step 5: Create Function-Based Views**

In your `todo` app, create function-based views in the `views.py` file to perform CRUD operations on tasks:

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

@api_view(['GET'])
def task_list(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def update_task(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=404)

    serializer = TaskSerializer(task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_task(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=404)

    task.delete()
    return Response(status=204)
```

**Step 6: Configure URLs**

Configure the URLs for your API in your project's `urls.py`:

```python
from django.urls import path, include
from todo.views import task_list, create_task, update_task, delete_task

urlpatterns = [
    path('api/', include('todo.urls')),
]
```

Then, in your `todo` app, create a `urls.py` file:

```python
from django.urls import path
from .views import task_list, create_task, update_task, delete_task

urlpatterns = [
    path('tasks/', task_list, name='task-list'),
    path('tasks/create/', create_task, name='create-task'),
    path('tasks/update/<int:pk>/', update_task, name='update-task'),
    path('tasks/delete/<int:pk>/', delete_task, name='delete-task'),
]
```

**Step 7: Run Migrations and Create Superuser**

Run database migrations to create the necessary database tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

Create a superuser account:

```bash
python manage.py createsuperuser
```

**Step 8: Start the Development Server**

Start the development server:

```bash
python manage.py runserver
```

**Step 9: Explore Your API**

You can now access your API endpoints:

- List of tasks: `http://localhost:8000/api/tasks/`
- Create a new task: `http://localhost:8000/api/tasks/create/`
- Update a task (replace `<pk>` with the task's primary key): `http://localhost:8000/api/tasks/update/<pk>/`
- Delete a task (replace `<pk>` with the task's primary key): `http://localhost:8000/api/tasks/delete/<pk>/`

You can use tools like Postman or a web browser to make requests to these endpoints to add, modify, and delete tasks. You can also use the Django admin panel to manage tasks.

This project provides a basic foundation for a RESTful API for task management. Further one can enhance it by adding authentication, pagination, filtering, and more as per your requirements.