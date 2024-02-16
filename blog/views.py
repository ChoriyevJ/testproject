from django.shortcuts import render
from rest_framework import generics


from blog.models import Post, Category
from blog.serializers import CategorySerializer, PostSerializer


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all().select_related('category')
    serializer_class = PostSerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

