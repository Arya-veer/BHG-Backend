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
        fields = ('photo','caption')

class PostListSerializer(serializers.ModelSerializer):
    images = PostImagesSerializer()

    class Meta:
        model = Post
        fields = ('static_id','title','text','images')

class PostImageListSerializer(PostListSerializer):
    images = PostImagesSerializer(many = True)

    class Meta:
        model = Post
        fields = PostListSerializer.Meta.fields + ('images',)

class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

class VideoListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = '__all__'

class FrontPageSerializer(serializers.ModelSerializer):

    class Meta:
        model = FrontPage
        fields = '__all__'

