from rest_framework import serializers
from .models import *

class CollegeListSerializer(serializers.ModelSerializer):

    class Meta:
        model = College
        fields = ("static_id","name","col_img")

class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ("static_id","name","categ_img")

class PostImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostImage
        fields = ('photo',)

class PostListSerializer(serializers.ModelSerializer):
    images = PostImagesSerializer(many = True)

    class Meta:
        model = Post
        fields = ('static_id','title','text','images')
