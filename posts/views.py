from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .models import *
from .serializers import *
# Create your views here.

class CollegeListAPI(generics.ListAPIView):

    permission_classes = (AllowAny,)
    serializer_class = CollegeListSerializer
    queryset = College.objects.all()

class CategoryListAPI(generics.ListAPIView):

    permission_classes = (AllowAny,)
    serializer_class = CategoryListSerializer
    
    def get_queryset(self):
        if "college_static_id" not in self.request.query_params:
            raise ValidationError("COLLEGE ID NOT PROVIDED")
        college = College.objects.filter(static_id = self.request.query_params["college_static_id"])
        if college.exists():
            college = college.first()
            category = Category.objects.filter(college=college)
            category = category.exclude(name = "GoodImages")

            return category
        else:
            raise ValidationError("INVALID COLLEGE ID GIVEN")

class PostListAPI(generics.ListAPIView):

    permission_classes = (AllowAny,)
    serializer_class = PostListSerializer
    
    def get_queryset(self):
        if "category_static_id" not in self.request.query_params:
            raise ValidationError("CATEGORY ID NOT PROVIDED")
        category = Category.objects.filter(static_id = self.request.query_params["category_static_id"])
        if category.exists():
            category = category.first()
            return Post.objects.filter(category=category)
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

