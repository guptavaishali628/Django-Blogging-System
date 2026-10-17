from django.shortcuts import render
from blogs.models import Category, Blog

# Create your views here.

# dashboards function
def dashboard(request):
    # category count
    category_count=Category.objects.all().count()
    # count blogs
    blogs_count=Blog.objects.all().count()

    context={
        'category_count':category_count,
        'blogs_count': blogs_count,
    }
    # print(category_count, blogs_count) # print the category count
    return render(request,'dashboard/dashboard.html', context)