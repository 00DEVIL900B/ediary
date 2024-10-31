from  django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add/', views.add, name='add'),
    path('create/', views.newDiary, name="newDiary"),
    path('delete_diary/', views.delete_diary, name="delete"),
    path('edit_diary/', views.edit_diary, name="edit"),
    path('edit/', views.edit, name="bedit"),
    path('search/', views.search, name="search"),
    path('view/<int:id>', views.view_diary, name="view"),
]
