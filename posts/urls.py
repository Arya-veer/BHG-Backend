from django.urls import path
from .views import *

urlpatterns = [
    path("colleges/",CollegeListAPI.as_view()),
    path("categories/",CategoryListAPI.as_view()),
    path("posts/",PostListAPI.as_view()),
]