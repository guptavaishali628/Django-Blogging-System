from django.shortcuts import render, redirect, get_object_or_404
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
    # first we see we are getting post request or not
    if request.method=='POST':
        form = CategoryForm(request.POST)
        # if form is valid then save
        if form.is_valid():
            form.save()
            return redirect('categories')
    # initialise the form to render in add_category.html
    form = CategoryForm()
    context={
        'form':form
    }
    return render(request, 'dashboard/add_category.html', context)

# Edit category function:
def edit_category(request,pk):
    # pass the instance so we get the name of category during the edit
    category = get_object_or_404(Category, pk=pk)
    if request.method=='POST':
        # take form data(request.post="newly value we are writing inside the form field ") and we also want to know what is the existing value had so we use(instance=category)
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    # pass the form to print to display
    form=CategoryForm(instance=category) # pass instance here
    context={
        'form':form,
        'category':category
    }
    return render(request, 'dashboard/edit_category.html', context)

# delete category function
def delete_category(request, pk):
    # take out the object from database and delete
    category=get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')