from django.urls import path
from djangoIntrocution.todo_app.views import index

urlpatterns = [
    path('', index),
]
