from django.db import models
# The built-in User model lives in django.contrib.auth.models:
from django.contrib.auth.models import User
# # to remove the slug error :
# from django.utils.text import slugify

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
    ('Draft', 'Draft'),
    ('Published', 'Published')
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
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Draft')
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # slug code
    # def save(self, *args, **kwargs):
    #     # Agar slug empty hai to title se slug banayenge
    #     if not self.slug:
    #         base_slug = slugify(self.title)
    #         slug = base_slug
    #         counter = 1
    #         # Check karein agar slug pehle se database me kisi aur post ke paas hai
    #         while Blog.objects.filter(slug=slug).exclude(pk=self.pk).exists():
    #             slug = f"{base_slug}-{counter}"
    #             counter += 1
    #         self.slug = slug
            
    #     super().save(*args, **kwargs)
    #-----------writing this slug code on views.py--------------->

    def __str__(self):
            return self.title

# create About model:
from django.db import models

class About(models.Model):
    about_heading = models.CharField(max_length=50, default="About Us")
    about_description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'About'

    def __str__(self):
        return self.about_heading

# class SocialLink
class SocialLink(models.Model):
    PLATFORM_CHOICES = (
        ('github', 'GitHub'),
        ('linkedin', 'LinkedIn'),
    )
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES, unique=True)
    link = models.URLField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.platform    
     
