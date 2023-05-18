"""
URL configuration for madblogger project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from madbloggerapp.views import UserAPIView, AuthorAPIView, BlogPostAPIView, CategoryAPIView, create_blogpost, blogpost_list, view_blogpost, delete_blogpost, edit_blogpost

urlpatterns = [
    path("admin/", admin.site.urls),

    path('create/', create_blogpost, name='create_blogpost'),
    path('list/', blogpost_list, name='blogpost_list'),
    path('view/<int:blogpost_id>/', view_blogpost, name='view_blogpost'),
    path('delete/<int:blogpost_id>/', delete_blogpost, name='delete_blogpost'),
    path('edit/<int:blogpost_id>/', edit_blogpost, name='edit_blogpost'),


    # Other URL patterns
    path('api/users/', UserAPIView.as_view(), name='user-api'),
    path('api/authors/', AuthorAPIView.as_view(), name='author-api'),
    path('api/blogposts/', BlogPostAPIView.as_view(), name='blogpost-api'),
    path('api/categories/', CategoryAPIView.as_view(), name='category-api'),


]
