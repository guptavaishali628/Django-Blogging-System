from django.shortcuts import redirect,render, get_object_or_404
from django.http import HttpResponse
from .models import Blog, Category

# Create your views here.

# function for posts_by_category
def posts_by_category(request, category_id):
    # fetch the posts that belpongs to the category with the id 'category_id'
    posts = Blog.objects.filter(status='Published', category=category_id)
    # fetch category name by category id:
    
    # if category do not found then handle error there are two methods
    
    # 1--> method (do not show the erroer page instead we redirect on homepage)
    try:
       category=Category.objects.get(pk=category_id)
    except:
        return render(request, '404.html')
    
    # 2nd--> method(show 404 error page if the category does not exist)
    # category = get_object_or_404(Category, pk=category_id)
    
    context= {
        'posts': posts,
        'category': category,
    }
 
    return render(request, 'post_by_category.html', context)

# function for single page blogs display
def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')
    context={
        'single_blog': single_blog,
    }
    return render(request, 'blogs.html', context)


