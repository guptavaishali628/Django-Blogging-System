"""
URL configuration for blog_main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views # this views inside the blog_main
from django.conf.urls.static import static
from django.conf import settings
from blogs import views as BlogView # this views inside the blogs

# all the request first come here
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    # here we are using urls from blogs app
    path('category/', include('blogs.urls')) ,
    # path for single page of specific cpost display with slug:(blogs/slug kreneg ni to regiser login function kaam ni krega)
    path('blogs/<slug:slug>/', BlogView.blogs, name='blogs'),  # blogs ye naam <a href={url 'blogs' post.slug}>

    # search end point
    path('blogs/search', BlogView.search, name='search'),

    # register url
    path('register/', views.register, name='register'),

    # login url
    path('login/', views.login, name='login'),

    # logout url
    path('logout/', views.logout, name='logout'),
    
    # reset_pass url
    path('reset_pass/', views.reset_pass, name='reset_pass'),

    # dashboard url pattern
    path('dashboard/', include('dashboards.urls')),

] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
