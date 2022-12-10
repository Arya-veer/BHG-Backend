from rest_framework import serializers
from .models import *

class CollegeListSerializer(serializers.ModelSerializer):

    class Meta:
        model = College
        fields = "__all__"

class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ("static_id","name","categ_img")

class PostImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostImage
        fields = ('photo',)

class PostListSerializer(serializers.ModelSerializer):
    # images = PostImagesSerializer(many = True)

    class Meta:
        model = Post
        fields = ('static_id','title','text')

class PostImageListSerializer(PostListSerializer):
    images = PostImagesSerializer(many = True)

    class Meta:
        model = Post
        fields = PostListSerializer.Meta.fields + ('images',)

