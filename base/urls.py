from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='list'),
    path("update-task/<int:pk>/", views.updateTask, name= 'update-task'),
    path("delete-task/<int:pk>/", views.deleteTask, name= 'delete-task')
]
