from django.urls import path
from .import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    
    # category Crud
    path('categories/', views.categories, name='categories' ),
    # add category path
    path('categories/add/',  views.add_category, name='add_category'),
    # edit category path
    path('categories/edit/<int:pk>',  views.edit_category, name='edit_category'),
    # delete category path
    path('categories/delete/<int:pk>',  views.delete_category, name='delete_category'),

    # blog post crud
    path('posts/', views.posts, name='posts' ),
]