from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('delete/<int:id>/', views.deletepost, name='deletepost'),
    path('search/', views.search, name='search'),
]
