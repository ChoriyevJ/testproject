from rest_framework import serializers

from blog.models import Post, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title',)


class PostSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(source="category.title")

    class Meta:
        model = Post
        fields = ('id', 'title', 'photo', 'is_active', 'created_at', 'category')
