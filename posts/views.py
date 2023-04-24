from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework import status

from .models import *
from .serializers import *
# Create your views here.

class CollegeListAPI(generics.ListAPIView):

    permission_classes = (AllowAny,)
    serializer_class = CollegeListSerializer
    queryset = College.objects.all()


class PostListAPI(generics.ListAPIView):

    permission_classes = (AllowAny,)
    serializer_class = PostListSerializer
    
    def get_queryset(self):
        if "category_static_id" not in self.request.query_params:
            raise ValidationError("CATEGORY ID NOT PROVIDED")
        college = College.objects.filter(static_id = self.request.query_params["college_static_id"])
        if college.exists():
            college = college.first()
            return Post.objects.filter(college=college)
        else:
            raise ValidationError("INVALID CATEGORY ID GIVEN")


    def list(self,request,*args, **kwargs):
        try:
            return super().list(request,*args, **kwargs)
        except ValidationError as e:
            return Response({"message":str(e)})

class PostImageListAPI(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = PostImagesSerializer
    
    def get_queryset(self):
        if "post_static_id" not in self.request.query_params:
            raise ValidationError("POST ID NOT PROVIDED")
        post = Post.objects.filter(static_id = self.request.query_params["post_static_id"])
        if post.exists():
            post = post.first()
            return PostImage.objects.filter(post=post)
        else:
            raise ValidationError("INVALID POST ID GIVEN")


    def list(self,request,*args, **kwargs):
        try:
            return super().list(request,*args, **kwargs)
        except ValidationError as e:
            return Response({"message":str(e)})


class BookListAPI(generics.ListAPIView):

    permission_classes = (AllowAny,)
    serializer_class = BookListSerializer
    queryset = Book.objects.all()

    def list(self,request,*args, **kwargs):
        try:
            return super().list(request,*args, **kwargs)
        except Exception as e:
            return Response({"message":str(e)})


class VideoListAPI(generics.ListAPIView):

    permission_classes = (AllowAny,)
    serializer_class = VideoListSerializer
    queryset = Video.objects.all()

    def list(self,request,*args, **kwargs):
        try:
            return super().list(request,*args, **kwargs)
        except Exception as e:
            return Response({"message":str(e)})

class FrontPageAPI(generics.RetrieveAPIView):

    permission_classes = (AllowAny,)
    serializer_class = FrontPageSerializer
    def get_object(self):
        return FrontPage.objects.all().first()
    
    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Exception as e:
            return Response({"message":str(e)})
        