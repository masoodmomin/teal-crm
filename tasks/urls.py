from django.urls import path
from . import views


urlpatterns = [
    path('', views.task, name="task"),
    path('add_task/', views.add_task, name="add_task"),
    path('del_task/<str:pk>', views.del_task, name="del_task"),

]
