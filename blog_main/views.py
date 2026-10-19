from django.http import HttpResponse
from django.shortcuts import render, redirect
from blogs.models import Category, Blog
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib import auth

def home(request):
    # fetch all the categories from database:
    # categories = Category.objects.all()  # coming from context_processor 
    # print(categories) # to print on shell
   
    # fetch featured_posts from database:
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('-updated_at')
    # print(featured_posts)

    # fetch not featured_posts:
    posts=Blog.objects.filter(is_featured=False, status='Published')
    print(posts)
   
    # send categories to home.html
    context = {
        # 'categories':  categories,
        'featured_posts': featured_posts,
        'posts': posts,
    }
    
    # return HttpResponse('<h2>Homepage</h2>')
    return render(request, 'home.html', context)

# register function
def register(request):
    # handle post req
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        # check form data is coming is valid or not
        if form.is_valid():
            # save the form
            form.save()
            return redirect('login')
        else:
            print(form.errors)  

    else:
        form = RegistrationForm()

    context={
        'form':form,
    }
    return render(request,'register.html', context)

# login function
def login(request):
    # check is req is post or not
    if request.method=='POST':
        form = AuthenticationForm(request, request.POST)  # enetring data inside the login form
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']

            # now we will take this user and password from  this and this authenticate and return the user
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect('dashboard')    

    # inbuilt login phone
    form = AuthenticationForm
    context={
        'form': form
    }
    return render(request, 'login.html', context)

# logout function
def logout(request):
    auth.logout(request)  # only take user
    return redirect('home')
# reset password
def reset_pass(request):
    form= PasswordResetForm()
    context={
        'form':form
    }
    return render(request, 'forget_password.html', context)