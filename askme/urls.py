from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
    path('askme', views.question_list, name='question_list'),
    path('create/', views.create),
]