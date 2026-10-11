from django.db import models
# The built-in User model lives in django.contrib.auth.models:
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Django Admin will display the section title as: "Categorys"
    class Meta :
        verbose_name_plural= 'categories'

    # In the Django Admin dashboard, dropdowns in foreign key fields, and debugging logs, every row will just say Category object (1),
    # Category object (2), making it impossible to tell them apart without clicking into each one.
    # string representation of this model and self is as category model:
    def __str__(self):
        return self.category_name  


    # Status choice should be draft or publish
STATUS_CHOICES=(
    (0, 'Draft'),
    (1, 'Published')
    )
# create Blog Model

class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  #taking refrence from table category
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='uploads/%y/%m/%d')
    short_description = models.TextField(max_length=500) 
    blog_body = models.TextField(max_length=500) 
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
     
