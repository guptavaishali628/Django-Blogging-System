from django.contrib import admin
from .models import Category, Blog

# prepopulated slug (here we will generate slug automatically based on title)
# and pass BlogAdmin in Blog register
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug': ('title',)}
    list_display = ('title', 'category', 'author', 'status', 'is_featured')
    # add search fields(here category is foreign key so we have to use 'category__category_name')
    search_fields = ('id', 'title', 'category__category_name', 'status')
    # add listeditable
    list_editable = ('is_featured',)

# Register your models here.
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)

