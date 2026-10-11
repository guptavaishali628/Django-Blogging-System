from django.contrib import admin
from .models import Category, Blog

# prepopulated slug (here we will generate slug automatically based on title)
# and pass BlogAdmin in Blog register
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug': ('title',)}

# Register your models here.
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)

