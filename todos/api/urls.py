from django.urls import path
from .views import (
    TodoListView,
    CreateTodoView,
    TodoDetailsView
)

urlpatterns = [
    path('all/', TodoListView.as_view(), name='todo-list-all'),
    path('create/', CreateTodoView.as_view(), name='create'),
    path('<int:pk>/',TodoDetailsView.as_view(),name='todo-details')

]
