from django.urls import path
from .views import list_Uni, insert, delete_task, update, update_from

urlpatterns = [
    path('', list_Uni),
    path("insert/", insert, name='insert'),
    path('update', update, name='update'),
    path('update/<int:task_id>/', update_from, name='update_from'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'), 
]
