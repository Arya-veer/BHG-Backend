from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework import status

from .models import *
from .serializers import *
from .pagination import VideoPagination
# Create your views here.

class CollegeListAPI(generics.ListAPIView):

    permission_classes = (AllowAny,)
    serializer_class = CollegeListSerializer
    queryset = College.objects.all()


class PostListAPI(generics.ListAPIView):

    permission_classes = (AllowAny,)
    serializer_class = PostListSerializer
    
    def get_queryset(self):
        if "college_static_id" not in self.request.query_params:
            raise Exception("COLLEGE ID NOT PROVIDED")
        college = College.objects.filter(static_id = self.request.query_params["college_static_id"])
        if college.exists():
            college = college.first()
            return Post.objects.filter(college=college)
        else:
            raise Exception("INVALID COLLEGE ID GIVEN")


    def list(self,request,*args, **kwargs):
        try:
            return super().list(request,*args, **kwargs)
        except Exception as e:
            return Response({"message":str(e)},status=status.HTTP_400_BAD_REQUEST)

class PostImageListAPI(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = PostImagesSerializer
    
    def get_queryset(self):
        if "post_static_id" not in self.request.query_params:
            raise Exception("POST ID NOT PROVIDED")
        post = Post.objects.filter(static_id = self.request.query_params["post_static_id"])
        if post.exists():
            return PostImage.objects.filter(post=post.first())
        else:
            raise Exception("INVALID POST ID GIVEN")


    def list(self,request,*args, **kwargs):
        try:
            return super().list(request,*args, **kwargs)
        except Exception as e:
            return Response({"message":str(e)},status=status.HTTP_400_BAD_REQUEST)


class BookListAPI(generics.ListAPIView):

    permission_classes = (AllowAny,)
    serializer_class = BookListSerializer
    queryset = Book.objects.all()

    def list(self,request,*args, **kwargs):
        try:
            return super().list(request,*args, **kwargs)
        except Exception as e:
            return Response({"message":str(e)},status=status.HTTP_400_BAD_REQUEST)


class VideoListAPI(generics.ListAPIView):

    permission_classes = (AllowAny,)
    serializer_class = VideoListSerializer
    queryset = Video.objects.all()
    pagination_class = VideoPagination

    def list(self,request,*args, **kwargs):
        try:
            return super().list(request,*args, **kwargs)
        except Exception as e:
            return Response({"message":str(e)},status=status.HTTP_400_BAD_REQUEST)

class FrontPageAPI(generics.RetrieveAPIView):

    permission_classes = (AllowAny,)
    serializer_class = FrontPageSerializer
    def get_object(self):
        return FrontPage.objects.all().first()
    
    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Exception as e:
            return Response({"message":str(e)},status=status.HTTP_400_BAD_REQUEST)
        