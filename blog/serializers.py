from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Post, Category

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'created_on', 'last_modified', 'categories', 'page_type']
    
    def validate(self, data):
        title = data["title"]

        if len(title) < 5:
            raise ValidationError("The title should be at least five characters.")
        
        return data
    
    def create(self, validated_data):
        categories = validated_data.pop("categories")

        post = Post(**validated_data)
        post.save()
        
        post.categories.set(categories)
        
        return post

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']