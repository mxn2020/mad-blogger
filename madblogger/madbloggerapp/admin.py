from django.contrib import admin
from .models import Author, BlogPost, Category

admin.site.register(Author)
admin.site.register(BlogPost)
admin.site.register(Category)
