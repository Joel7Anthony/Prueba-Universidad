from django.urls import path
from .views import list_Uni, create_task, delete_task, editar_task

urlpatterns = [
    path('', list_Uni),
    path('new_task/', create_task, name='create_task'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
    path('editar_task/<int:task:id/', editar_task, name='editar_task' )
]
