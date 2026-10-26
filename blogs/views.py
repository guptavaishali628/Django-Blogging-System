from django.shortcuts import redirect,render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Blog, Category, Comment
# the Q objects allows u to makes the complex lookups such as OR operations
from django.db.models import Q

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

    # add comment
    if request.method=='POST':
        comment=Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info) # this will take u to the same page

    # comments
    comments=Comment.objects.filter(blog=single_blog)
    # print('Comments:' , comments)
    # count comment
    comment_count = comments.count()
    context={
        'single_blog': single_blog,
        'comments': comments,
        'comment_count':comment_count
    }
    return render(request, 'blogs.html', context)

# Search function
def search(request):
    # ye keyword yha se get kr rhe hai url se http://127.0.0.1:8000/blogs/search?keyword=socially
    keyword = request.GET.get('keyword')
    # print("keyword",keyword) # printing on console
    # now we will match this keyword from blogs
    # fetch the blog
    # blogs=Blog.objects.filter(title__contains=keyword, status="Published")  # here , represent and operator when  the both conditions are true then the code will run

    # use of Q functions
    blogs=Blog.objects.filter(Q(title__icontains=keyword) | 
                              Q(short_description__icontains=keyword) | 
                              Q(blog_body__icontains=keyword), 
                              status="Published"
    )
    # print(blogs)

    context={
        'blogs': blogs,
        'keyword': keyword
    }
    return render(request, 'search.html', context)

