from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('create_task', views.CreateTask.as_view(), name='create_task'),
    #path('edit_task/<int:id>', views.EditTask.as_view(), name='edit_task'),
    path('edit_task/<int:pk>', views.EditTask.as_view(), name='edit_task'),
    path('delete_task/<int:pk>', views.DeleteTask.as_view(), name='delete_task'),

]
