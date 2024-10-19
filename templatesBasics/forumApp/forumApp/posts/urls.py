from django.urls import path
from forumApp.posts.views import dashboard, index

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dash'),
]
