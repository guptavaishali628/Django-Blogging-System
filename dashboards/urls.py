from django.urls import path
from .import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    # category path
    path('categories/', views.categories, name='categories' ),
    # add category path
    path('categories/add/',  views.add_category, name='add_category'),
    # edit path
    path('categories/edit/<int:pk>',  views.edit_category, name='edit_category'),

]