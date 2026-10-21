from django.shortcuts import render, redirect, get_object_or_404
from blogs.models import Category, Blog
# import decorators
from django.contrib.auth.decorators import login_required

# importing category form
from dashboards.forms import CategoryForm, BlogPostForm

# for slug error handle import slugify function
from django.template.defaultfilters import slugify

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

# Blog posts function
def posts(request):
    # fetch all the posts 
    posts=Blog.objects.all()
    context={
        'posts':posts,
    }

    return render(request, 'dashboard/posts.html', context)

# add blog posts
def add_post(request):
    # we will receive the post request here from form in add_post.html
    if request.method=='POST':
        form=BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            # here we want to add custom data to this form.
            # temporary saving the form
            post = form.save(commit=False)  #commit=false actually give us the model object which is post
            # inside the post object we get author field(who is author? the person logged in)
            post.author = request.user
            # now save the post.save()instead saving form:
            # post.save()
            # print("valid form")
            # form.save()
            # put the title inside the slugify function
            title=form.cleaned_data['title']
            post.slug=slugify(title) + '-'+str(post.id) # to make it unique
            post.save()
            
            return redirect('posts')
        else:
            # print("form is invalid")
            print(form.errors)
    form=BlogPostForm()
    context={
        'form':form,
    }
    return render(request,'dashboard/add_post.html', context)

# edit blog posts
def edit_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            title=form.cleaned_data['title']
            post.slug = slugify(title)+ '_'+str(post.id)
            post = form.save()
            return redirect('posts')
        
    form = BlogPostForm(instance=post)

    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'dashboard/edit_post.html', context)

# Delete blog posts
def delete_post(request):
    return render(request,'dashboard/delete_post.html')

