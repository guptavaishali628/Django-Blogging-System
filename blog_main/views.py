from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Category, Blog

def home(request):
    # fetch all the categories from database:
    categories = Category.objects.all()
    # print(categories) # to print on shell
   
    # fetch featured_posts from database:
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('-updated_at')
    # print(featured_posts)

    # fetch not featured_posts:
    posts=Blog.objects.filter(is_featured=False, status='Published')
    # print(posts)  
   
    # send categories to home.html
    context = {
        'categories':  categories,
        'featured_posts': featured_posts,
        'posts': posts,
    }
    
    # return HttpResponse('<h2>Homepage</h2>')
    return render(request, 'home.html', context)