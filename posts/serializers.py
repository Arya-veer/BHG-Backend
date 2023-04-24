from rest_framework import serializers
from .models import *

class CollegeListSerializer(serializers.ModelSerializer):

    class Meta:
        model = College
        fields = "__all__"

class PostImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostImage
        fields = ('photo','caption')

class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = "__all__"


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

