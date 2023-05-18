from django.shortcuts import render, get_object_or_404, redirect

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Author, BlogPost, Category
from .serializers import UserSerializer, AuthorSerializer, BlogPostSerializer, CategorySerializer

def delete_blogpost(request, blogpost_id):
    # Fetch the blog post with the given ID from the database
    blogpost = get_object_or_404(BlogPost, id=blogpost_id)
    
    if request.method == 'POST':
        # Delete the blog post
        blogpost.delete()
        
    # Redirect the user to the blog post list page
    return redirect('blogpost_list')

def edit_blogpost(request, blogpost_id):
    # Fetch the blog post with the given ID from the database
    blogpost = get_object_or_404(BlogPost, id=blogpost_id)
    
    if request.method == 'POST':
        # Update the blog post with the form data
        title = request.POST.get('title')
        content = request.POST.get('content')
        blogpost.title = title
        blogpost.content = content
        blogpost.save()
        
        # Redirect the user to the updated blog post view page
        return redirect('view_blogpost', blogpost_id=blogpost.id)
    
    # Render the edit blog post form
    return render(request, 'madbloggerapp/edit_blogpost.html', {'blogpost': blogpost})


def create_blogpost(request):
    if request.method == 'POST':
        # Process the form data and create a new blog post
        title = request.POST.get('title')
        content = request.POST.get('content')
        user = request.user

        # Check if the Author object exists for the current user
        try:
            author = user.author
        except Author.DoesNotExist:
            # If the Author object doesn't exist, create it
            author = Author.objects.create(user=user)

        blogpost = BlogPost.objects.create(title=title, content=content, author=author)

        # Redirect the user to the newly created blog post page
        return redirect('view_blogpost', blogpost_id=blogpost.id)
    else:
        # Render the create blog post form
        return render(request, 'madbloggerapp/create_blogpost.html')

def blogpost_list(request):
    # Fetch all the blog posts from the database
    blogposts = BlogPost.objects.all()
    return render(request, 'madbloggerapp/blogpost_list.html', {'blogposts': blogposts})


def view_blogpost(request, blogpost_id):
    # Fetch the blog post with the given ID from the database
    blogpost = get_object_or_404(BlogPost, id=blogpost_id)
    return render(request, 'madbloggerapp/view_blogpost.html', {'blogpost': blogpost})



class UserAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AuthorAPIView(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogPostAPIView(APIView):
    def get(self, request):
        blogposts = BlogPost.objects.all()
        serializer = BlogPostSerializer(blogposts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Define similar views for BlogPost and Category models
