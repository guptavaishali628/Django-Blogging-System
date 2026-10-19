from django.shortcuts import render
from blogs.models import Category, Blog
# import decorators
from django.contrib.auth.decorators import login_required

# importing category form
from dashboards.forms import CategoryForm

# Create your views here.

# dashboards function
# apply decorator to restrict action
@login_required(login_url='login')
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

# category function
def categories(request):
    return render(request, 'dashboard/categories.html')

# add category function
def add_category(request):
    # initialise the form to render in add_category.html
    form = CategoryForm()
    context={
        'form':form
    }
    return render(request, 'dashboard/add_category.html', context)