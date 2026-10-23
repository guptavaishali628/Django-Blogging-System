# using model form
from django import forms
from blogs.models import Category, Blog, User
from django.contrib.auth.forms import UserCreationForm

# create category form
class CategoryForm(forms.ModelForm):
    # create class meta which will take model category
    class Meta:
        model=Category
        fields='__all__'

# create posts form:
class BlogPostForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=('title','category','featured_image','short_description', 'blog_body', 'status', 'is_featured')   

# create user form
class AddUserForm(UserCreationForm):
    class Meta:
        model= User
        fields=('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')

