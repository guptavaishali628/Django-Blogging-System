# using model form
from django import forms
from blogs.models import Category

# create category form
class CategoryForm(forms.ModelForm):
    # create class meta which will take model category
    class Meta:
        model=Category
        fields='__all__'