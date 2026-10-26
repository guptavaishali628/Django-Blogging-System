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
    # add blog post
    path('posts/add', views.add_post, name='add_post'),
    # edit blog post
    path('posts/edit/<int:pk>', views.edit_post, name='edit_post'),
    # delete blog post
    path('posts/delete/<int:pk>', views.delete_post, name='delete_post'),

    # users
    path('users/', views.users, name='users' ),
    # add user path
    path('users/add',views.add_user, name='add_user'),
    # edit user path
    path('users/edit/<int:pk>', views.edit_user, name='edit_user'),
    #delete user path
    path('users/delete/<int:pk>',views.delete_user, name='delete_user')

]