from rest_framework import serializers
from .models import Post, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class PostSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'created_on', 'last_modified', 'categories', 'page_type']
    
    def create(self, validated_data):
        categories = validated_data.pop("categories")

        categories_ids = [category["id"] for category in categories]

        post = Post(**validated_data)
        post.save()
        
        post.categories.set(categories_ids)
        
        return post