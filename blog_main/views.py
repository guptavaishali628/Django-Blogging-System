from django.http import HttpResponse
from django.shortcuts import render, redirect
from blogs.models import Category, Blog
from .forms import RegistrationForm

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
            return redirect('register')
        else:
            print(form.errors)  

    else:
        form = RegistrationForm()

    form = RegistrationForm()
    context={
        'form':form,
    }
    return render(request,'register.html', context)