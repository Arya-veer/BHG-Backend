from django.http import HttpResponse
from wsgiref.util import FileWrapper
from Library_backend.settings import MEDIA_ROOT
from rest_framework import serializers
from .models import *
import PyPDF2

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

    pages = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = ("static_id","title","author","description","bookFile","book_cover","pages")

    def get_pages(self,obj):
        file = open(obj.bookFile.path,'rb')
        pdfReader = PyPDF2.PdfReader(file)
        return len(pdfReader.pages)



class VideoListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = '__all__'

class FrontPageSerializer(serializers.ModelSerializer):

    class Meta:
        model = FrontPage
        fields = '__all__'

class FooterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Footer
        fields = '__all__'
