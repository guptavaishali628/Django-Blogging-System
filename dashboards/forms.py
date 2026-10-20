# using model form
from django import forms
from blogs.models import Category, Blog

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